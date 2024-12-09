import logging

from aiogram import Bot
from aiogram.types import BotCommand

logger = logging.getLogger(__name__)

async def set_menu(bot: Bot) -> None:

    menu = [
        BotCommand(command='/help', description='Руководство по боту'),
        BotCommand(command='/continue', description='Продолжить чтение'),
        BotCommand(command='/beginning',  description='Перейти в начало книги'),
        BotCommand(command='/bookmarks', description='Твои закладки по книге')]

    logger.info('init set menu')
    await bot.set_my_commands(menu)

