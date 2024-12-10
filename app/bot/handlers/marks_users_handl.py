import logging

from aiogram import F, Router, types, filters

from app.bot.databases.database import User, BookMarks
from app.bot.keyboards.inlinekeyboard import load_inline_keyboard
from app.bot.lexicons.lexicon import LEXICON

router: Router = Router()
logger = logging.getLogger(__name__)


@router.message(filters.Command(commands='bookmarks'))
async def get_mark(message: types.Message, mark: BookMarks) -> None:

    logger.debug(f'{mark, mark.get_mark()}')
    if not mark.check_mark():
        await message.answer(text=LEXICON['not_marks'])

    else:
        build = load_inline_keyboard((1,), **mark.get_mark(), repeat=True)
        build_edit_cancel = load_inline_keyboard((2,), **{'Редактировать': 'edit', 'Вернуться': 'cancel'})
        build.attach(build_edit_cancel)
        await message.answer(text='Вот твои закладки. При нажатии ты сможешь перейти к этой странице',
                             reply_markup=build.as_markup())





@router.callback_query(F.data == '/bookmarks')
async def call_mark(callback: types.CallbackQuery, user: User, mark: BookMarks) -> None:

    mark.number_page = user.number_page
    mark.save_mark(callback.message.text)
    logger.debug(f'{mark.get_mark()}')
    logger.debug(f'{mark}')
