import logging

from aiogram import filters, types

logger = logging.getLogger(__name__)


class SearchNumber(filters.BaseFilter):

    async def __call__(self, callback: types.CallbackQuery) -> dict[str, int] | bool:

        number = int(callback.data.split('/')[0])
        if number:
            return {'number': number}
        return False