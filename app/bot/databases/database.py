import logging

from app.bot.lexicons.lexicon import BUTTONS

logger = logging.getLogger(__name__)


class User:

    def __init__(self, number_page: int) -> None:
        self.number_page = number_page

    def next_page(self) -> None:
        if len(BUTTONS) != self.number_page:
            self.number_page += 1

    def back_page(self) -> None:
        if self.number_page != 1:
            self.number_page -= 1

    def begin_page(self) -> None:
        self.number_page = 1


class BookMarks(User):

    def __init__(self, mark: dict[int, str] | None, number_page: int | None = None) -> None:
        super().__init__(number_page=number_page)
        self.mark = mark

    def get_mark(self) -> dict[int, str]:
        return self.mark

    def save_mark(self, page: str):
        self.mark[self.number_page] = page

    def delete(self, num_page):
        if num_page in self.mark:
            del self.mark[num_page]
        else:
            raise ValueError('данный ключ не содержиться в BookMarks')
