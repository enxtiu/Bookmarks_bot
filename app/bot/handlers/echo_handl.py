import logging

from aiogram import Router, types
from app.bot.lexicons.lexicon import LEXICON

router: Router = Router()
logger = logging.getLogger(__name__)

@router.message()
@router.callback_query()
async def echo(message: types.Message) -> None:
    await message.answer(LEXICON['echo'])



