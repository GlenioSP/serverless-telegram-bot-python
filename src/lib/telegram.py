import logging
import os
import telegram

logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)


class TelegramService:
    def __init__(self):
        logger.info(os.environ)
        self.token = os.environ.get('TELEGRAM_TOKEN')

    def configure_telegram(self):
        """
        Configures the bot with a Telegram Token.
        Returns a bot instance.
        """

        if not self.token:
            logger.error('The TELEGRAM_TOKEN must be set.')
            raise NotImplementedError

        return telegram.Bot(self.token)
