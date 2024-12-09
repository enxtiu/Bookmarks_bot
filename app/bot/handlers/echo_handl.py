import logging

from aiogram import Router, types
from app.bot.lexicons.lexicon import LEXICON

router: Router = Router()
logger = logging.getLogger(__name__)

@router.message()
async def echo(message: types.Message) -> None:
    await message.answer(LEXICON['echo'])

@router.callback_query()
async def echo_call(callback: types.CallbackQuery) -> None:
    await callback.answer(text='ой, что-то не так')

