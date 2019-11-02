# lambda line bot template

This is a template for creating a LINE bot with AWS Lambda.

## Requirement

- [Docker](https://www.docker.com/)
  - docker-compose

## Usage

Setup on AWS:

ref(Japanese only)
- [Lambdaでline-bot-sdk-pythonを使用してオウム返しBOTを作成する](https://qiita.com/konikoni428/items/fd1ab5993bc5526726bb)

Lambda upload:

```console
$ docker-compose run awscli bash
> lambda-uploader
```

## Install

Clone repository:

```console
$ git clone https://github.com/PiroHiroPiro/lambda_line_bot_template.git
$ cd lambda_line_bot_template
```

Build image:

```console
$ cp .env.example .env
$ cp lambda.json.example ./source/lambda.json
$ docker-compose build
```

## Licence

This software is released under the MIT License, see [LICENSE](https://github.com/PiroHiroPiro/lambda_line_bot_template/blob/master/LICENSE).

## Author

[Hiroyuki Nishizawa](https://github.com/PiroHiroPiro)
