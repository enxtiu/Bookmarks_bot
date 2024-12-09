import logging

logger = logging.getLogger(__name__)

class User:

    def __init__(self, _id_user: int, _number_page: int) -> None:
        self._id_user = _id_user
        self._number_page = _number_page



class BookMarks(User):

    def __init__(self, _id_user: int, number_page: int, mark: str) -> None:
        super().__init__(_id_user, number_page)