[![Build Status](https://travis-ci.org/Svinci131/wadsworth-twebhook.svg?branch=master)](https://travis-ci.org/Svinci131/wadsworth-twebhook) [![Coverage Status](https://coveralls.io/repos/github/Svinci131/wadsworth-twebhook/badge.svg?branch=travis)](https://coveralls.io/github/Svinci131/wadsworth-twebhook?branch=travis)

[![twebhook](https://github.com/Svinci131/wadsworth/blob/master/assets/twehbook.png?raw=true)](https://github.com/Svinci131/wadsworth/blob/master/assets/twebhook_attribution.md) [![arrow](https://github.com/Svinci131/wadsworth/blob/master/assets/right_arrow.png?raw=true)](https://github.com/Svinci131/wadsworth/blob/master/assets/right_arrow_attribution.md) [![butler](https://github.com/Svinci131/wadsworth/blob/master/assets/butler.png?raw=true)](https://github.com/Svinci131/wadsworth/blob/master/assets/butler_attribution.md)

## TWEBHOOK

*Twilio webhook for communicating with internally established rpi services*

## How it works

When a text is sent to a prespecified twilio number, twilio invokes a webhook (configured in their settings). This webhook points to a deployed AWS Lambda function (in this case, `hello.handler`) that parses the text message body and depending on the contents, routes the call to a raspberry pi endpoint. 

In particular, this is a useful technique for allowing a singular interface for interacting with multiple DIY smart home projects that sit inside (or is only accessible within) a wifi network.

## Getting Started

Implementation is deployed to AWS Lambda via the Serverless Framework. Twilio is leveraged for actual SMS communication. 

## Set up
Before beginning, key services must be configured.

### Configure Serverless Framework/AWS account
We used **[this](https://serverless.com/framework/docs/providers/aws/guide/credentials#setup-with-the-aws-cli)** Serverless Framework tutorial to configure our AWS credentials.

### Configure Twilio
**TODO**.

## Run Tests
Before pushing, it is a good idea to run tests.

```
docker-compose run test
```

## Deploy
To deploy to AWS lambda,
```
docker-compose run deploy
```

*This project is a **[wadsworth](https://github.com/Svinci131/wadsworth)** service.*
