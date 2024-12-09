import logging

from aiogram import Router, types, filters, F

from app.bot.keyboards.inlinekeyboard import load_inline_keyboard, buttons
from app.bot.lexicons.lexicon import BUTTONS, NAME_1, NAME_2
from app.bot.databases.database import User

router: Router = Router()
logger = logging.getLogger(__name__)

@router.message(filters.Command(commands='beginning'))
async def get_begin_book(message: types.Message, user: User) -> None:
    user.begin_page()
    await message.answer(
        text=f'{NAME_1}\n\n\n{NAME_2}',
        reply_markup=load_inline_keyboard(**buttons)
    )

@router.message(filters.Command(commands='continue'))
async def get_continue_book(message: types.Message, user: User) -> None:
    for k, v in BUTTONS.items():
        if user.number_page == k:
            await message.answer(
                text=v,
                reply_markup=load_inline_keyboard(**{'<<':'-1', f'{k}/{len(BUTTONS)}':'/bookmarks', '>>':'1'}))
            return

    logger.info('Пользователь ещё не читал')
    await get_begin_book(message, user)

@router.callback_query(F.data == '-1')
async def back_page(callback: types.CallbackQuery, user: User) -> None:
    page = user.number_page
    user.back_page()
    if page == user.number_page:
        await callback.answer(text='Ты уже на первой странице, назад идти некуда')
    else:
        await callback.message.edit_text(
            text=f'{BUTTONS[user.number_page]}',
            reply_markup=load_inline_keyboard(
                **{'<<':'-1', f'{user.number_page}/{len(BUTTONS)}':'/bookmarks', '>>':'1'})
        )

@router.callback_query(F.data == '1')
async def next_page(callback: types.CallbackQuery, user: User) -> None:
    page = user.number_page
    user.next_page()
    if page == user.number_page:
        await callback.answer(text='Ты уже на последней странице, вперёд идти некуда')
    else:
        await callback.message.edit_text(
            text=f'{BUTTONS[user.number_page]}',
            reply_markup=load_inline_keyboard(
                **{'<<': '-1', f'{user.number_page}/{len(BUTTONS)}': '/bookmarks', '>>': '1'}
            )
        )