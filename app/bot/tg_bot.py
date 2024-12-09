import logging

from aiogram import Bot, Dispatcher

from app.bot.configs.config_data import load_config, Config
from app.bot.databases.database import User
from app.bot.handlers import users_handl, menu, echo_handl

logger = logging.getLogger(__name__)

async def main() -> None:

    config: Config = load_config()

    logger.info('init bot, dp')
    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()
    dp.workflow_data.update({'user': User(1, None)})


    await menu.set_menu(bot)
    logger.info('register menu')
    dp.startup.register(menu.set_menu)

    logger.info('connection router_user')
    dp.include_router(users_handl.router)

    dp.include_router(echo_handl.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

