with open(r'C:\Users\Redmi\PycharmProjects\Bookmarks\book.txt', encoding='utf-8', errors='replace') as file:
   file = file.readlines()


NAME_1 = file[0]
NAME_2 = file[1]
BUTTONS = {str(k):v.rstrip() for k, v in enumerate(file[2:], start=2)}
