with open(r'C:\Users\Redmi\PycharmProjects\Bookmarks\book.txt', encoding='utf-8', errors='replace') as file:
   file = file.readlines()


NAME_1 = file[0]
NAME_2 = file[1]
BUTTONS = {k:v.rstrip() for k, v in enumerate(file[2:], start=2)}
LEXICON = {
   '/start': """Привет, что сегодня собираешься почитать?
Могу предложить Антона Павловича Чехова и его рассказ О любви
Для руководстава можешь использовать команду /help""",
   '/help': """Это бот читалка
Доступные команды:
/help - руководство по боту
/continue - продолжить чтение
/beginning - перейти в начало книги
/bookmarks - твои закладки по книге""",
   'echo': 'Воспользуйся командой /continue, чтобы продолжить чтение'
}