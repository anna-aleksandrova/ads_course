
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

size: int =  1000003
count: int
keys: list[None | str]
values: list[set[str]]

prime = 61

def hash(s):
    h = 0
    for i in range(len(s)):
        h = (h * prime + ord(s[i])) % size
    return h

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global count, keys, values
    count = 0
    keys = [None for _ in range(size)]
    values = [set() for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global count
    current = hash(author)
    while keys[current] is not None:
        if keys[current] == author:
            values[current].add(title)
            return
        current = (current + 1) % size
    keys[current] = author
    values[current].add(title)
    count += 1


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    current = hash(author)
    while keys[current] is not None:
        if keys[current] == author:
            if title in values[current]:
                return True
            else:
                return False
        current = (current + 1) % size
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    current = hash(author)
    while keys[current] is not None:
        if keys[current] == author:
            values[current].remove(title)
            return
        current = (current + 1) % size
    return


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    current = hash(author)
    while keys[current] is not None:
        if keys[current] == author:
            return sorted(list(values[current]))
        current = (current + 1) % size
    return []
