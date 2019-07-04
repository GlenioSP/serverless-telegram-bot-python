## Usage

**What do I need?**

- A AWS key configured locally, see [here](https://serverless.com/framework/docs/providers/aws/guide/credentials/)
- NodeJS 8+
- A Telegram account

## Installing

```
# Install the Serverless Framework
$ npm i -g serverless

# Inside the project root folder install the necessary plugins
$ npm i

# Get a bot from Telegram, sending this message to @BotFather
$ /newbot

# Put the token received into a file called .env.yml in your project's root folder, like the .env.example file:
$ cat .env.yml
TELEGRAM_TOKEN: <your_token>

# Deploy it!
$ serverless deploy -v

or if using a profile

$ serverless deploy -v --aws-profile your_profile_name

# With the API Gateway URL returned in the output, configure the Webhook
$ curl -X POST https://<your_url>.amazonaws.com/dev/set_webhook
```

Now, just start a conversation with the bot :)

## Based on

[Serverless Telegram Bot](https://github.com/serverless/examples/tree/master/aws-python-telegram-bot)
