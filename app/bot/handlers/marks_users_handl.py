import logging

from aiogram import F, Router, types, filters

from app.bot.databases.database import User, BookMarks
from app.bot.keyboards.inlinekeyboard import load_inline_keyboard
from app.bot.lexicons.lexicon import LEXICON
from app.bot.filters.filter import SearchNumber
from app.bot.lexicons.lexicon import BUTTONS

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


@router.callback_query(F.data == 'edit')
async def call_edit(callback: types.CallbackQuery, mark: BookMarks) -> None:

    result ={f'удалить закладку {k.split(':')[0]}': f'{k.split(':')[0]}/del' for k in mark.get_mark()}
    logger.debug(f'{result}')

    build = load_inline_keyboard((1,), repeat=True, **result)
    build_cancel = load_inline_keyboard((1,), **{'Вернуться': 'cancel'})
    build.attach(build_cancel)
    await callback.message.edit_text(text='Нажми на ту закладку которую хочешь удалить',
                                     reply_markup=build.as_markup())

@router.callback_query(F.data == 'cancel')
async def call_cancel(callback: types.CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer(text='Чтобы продолжить чтение воспользуйся командой /continue')

@router.callback_query(F.data.split('/')[1] == 'mark_id', SearchNumber())
async def call_continue(callback: types.CallbackQuery, number: int) -> None:
    for k, v in BUTTONS.items():
        if number == k:
            await callback.message.edit_text(
                text=v,
                reply_markup=load_inline_keyboard(**{'<<':'-1', f'{k}/{len(BUTTONS)}':'/bookmarks', '>>':'1'}).as_markup())
            return

@router.callback_query(F.data.split('/')[1] == 'del', SearchNumber())
async def call_dell(callback: types.CallbackQuery, mark: BookMarks, number: int):
    mark.delete(number)
    result = {f'удалить закладку {k.split(':')[0]}': f'{k.split(':')[0]}/del' for k in mark.get_mark()}
    build = load_inline_keyboard((1,), repeat=True, **result)
    build_cancel = load_inline_keyboard((1,), **{'Вернуться': 'cancel'})
    build.attach(build_cancel)


    await callback.message.edit_text(text=callback.message.text,
                                     reply_markup=build.as_markup())


@router.callback_query(F.data == '/bookmarks')
async def call_mark(callback: types.CallbackQuery, user: User, mark: BookMarks) -> None:

    mark.number_page = user.number_page
    mark.save_mark(callback.message.text)
    logger.debug(f'{mark.get_mark()}')
    logger.debug(f'{mark}')
    await callback.answer(text='Вы точно хотели бы добавить эту страницу в закладки?', show_alert=True)

