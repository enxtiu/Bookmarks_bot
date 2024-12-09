import logging

from aiogram import Bot, Dispatcher

from app.bot.configs.config_data import load_config, Config
from app.bot.databases.database import User

logger = logging.getLogger(__name__)

async def main() -> None:

    config: Config = load_config()

    logger.info('init bot, dp')
    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()
    dp.workflow_data.update({'user': User(1, None)})


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

