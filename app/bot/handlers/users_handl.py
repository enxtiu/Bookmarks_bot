import logging

from aiogram import Router, types, filters
from app.bot.lexicons.lexicon import LEXICON

logger = logging.getLogger(__name__)

logger.info('init user_handler router')
router: Router = Router()

@router.message(filters.CommandStart())
async def get_start(message: types.Message) -> None:
    await message.answer(LEXICON['/start'])

@router.message(filters.Command(commands='help'))
async def get_help(message: types.Message) -> None:
    await message.answer(LEXICON['/help'])