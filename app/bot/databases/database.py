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

    def __init__(self, mark: dict[int, str], number_page: int | None = None, count_marks: int = 2) -> None:
        super().__init__(number_page=number_page)
        self.mark = mark
        self.count_marks = len(self.mark) + count_marks

    def get_mark(self) -> dict[str, str]:
        logger.debug(f'{self.mark}')
        return {f'{k}: {v}': f'{k}/mark_id' for k, v in self.mark.items()}

    def check_mark(self) -> bool:
        return bool(self.mark)

    def save_mark(self, page: str):
        self.count_marks += 1
        self.mark[self.number_page] = page

    def delete(self, num_page: int):
        if num_page in self.mark:
            self.count_marks -= 1
            self.mark.pop(num_page)
        else:
            raise ValueError('данный ключ не содержиться в BookMarks')
