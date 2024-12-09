import logging

from app.bot.lexicons.lexicon import BUTTONS
logger = logging.getLogger(__name__)

class User:

    def __init__(self, number_page: int, mark: list[str, str] | None) -> None:
        self.number_page = number_page
        self.mark = mark

    def get_mark(self) -> list[str, str]:
        return self.mark

    def next_page(self) -> None:
        if len(BUTTONS) != self.number_page:
            self.number_page += 1

    def back_page(self) -> None:
        if self.number_page != 1:
            self.number_page -= 1

