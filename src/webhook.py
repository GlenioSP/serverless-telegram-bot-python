import json
import telegram
import logging

from src.main.lib.telegram import TelegramService

logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

telegram_service = TelegramService()

WEBHOOK_SET_OK_RESPONSE = 'Webhook configured successfully.'

WEBHOOK_SET_ERROR_RESPONSE = 'Oops, something went wrong while configuring the webhook.'


def handler(event, context):
    """
    Runs the Telegram webhook.
    """

    bot = telegram_service.configure_telegram()
    logger.info(f'Event: {event}')

    if event.get('httpMethod') == 'POST' and event.get('body'):
        logger.info('Message received')
        update = telegram.Update.de_json(json.loads(event.get('body')), bot)
        chat_id = update.message.chat.id
        text = update.message.text

        if text == '/start':
            yum_emoji = u'\U0001F60B'
            text = f'''Hey, hello! I could be a bot to order some food {yum_emoji}'''

        bot.sendMessage(chat_id=chat_id, text=text)
        logger.info('Message sent')

        return _build_return_response(200, WEBHOOK_SET_OK_RESPONSE)
    return _build_return_response(400, WEBHOOK_SET_ERROR_RESPONSE)


def set_webhook(event, context):
    """
    Sets the Telegram bot webhook.
    """

    logger.info(f'Event: {event}')
    bot = telegram_service.configure_telegram()
    url = 'https://{}/{}/'.format(
        event.get('headers').get('Host'),
        event.get('requestContext').get('stage'),
    )
    webhook = bot.set_webhook(url)

    if webhook:
        return _build_return_response(200, WEBHOOK_SET_OK_RESPONSE)
    return _build_return_response(400, WEBHOOK_SET_ERROR_RESPONSE)


def _build_return_response(status, message):
    return {
        'statusCode': status,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
    }
