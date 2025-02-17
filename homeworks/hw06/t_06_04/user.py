
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class Node:
    def __init__(self, key: str, value: set):
        self.key = key
        self.value = {value}
        self.next = None

size: int = 101
slots: list[None | Node]
prime: int = 31

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots, size
    slots = [None for _ in range(size)]

def hash(S: str):
    h = 0
    for i in range(len(S)):
        h = ((h * prime) + ord(S[i])) % size
    return h

def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    current = hash(author)
    node = slots[current]
    while node is not None:
        if node.key == author:
            node.value.add(title)
            return
        node = node.next
    node = Node(author, title)
    node.next = slots[current]
    slots[current] = node


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    current = hash(author)
    node = slots[current]
    while node is not None:
        if node.key == author:
            if title in node.value:
                return True
            else:
                return False
        node = node.next
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    current = hash(author)
    node = slots[current]
    while node is not None:
        if node.key == author:
            node.value.discard(title)
            break
        node = node.next
        

def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    current = hash(author)
    node = slots[current]
    while node is not None:
        if node.key == author:
            return sorted(list(node.value))
        node = node.next
    return []

