import os
import sys
import logging

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)


logger = logging.getLogger()
logger.setLevel(logging.ERROR)

line_channel_secret_key = os.getenv('LINE_CHANNEL_SECRET_KEY', None)
line_channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if line_channel_secret_key is None:
    logger.error('Specify LINE_CHANNEL_SECRET_KEY as environment variable.')
    sys.exit(1)
if line_channel_access_token is None:
    logger.error('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(line_channel_access_token)
handler = WebhookHandler(line_channel_secret_key)


def lambda_handler(event, context):
    signature = event["headers"]["X-Line-Signature"]
    body = event["body"]
    ok_json = {"isBase64Encoded": False,
               "statusCode": 200,
               "headers": {},
               "body": ""}
    error_json = {"isBase64Encoded": False,
                  "statusCode": 403,
                  "headers": {},
                  "body": "Error"}

    @handler.add(MessageEvent, message=TextMessage)
    def message(line_event):
        text = line_event.message.text
        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=text))

    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        logger.error("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            logger.error("  %s: %s" % (m.property, m.message))
        return error_json
    except InvalidSignatureError:
        return error_json

    return ok_json
