# Поиск в ширину, используя хеш-таблицы (словари) и двусторонние очереди.
# Здесь нам нужно найти продавца манго среди друзей и друзей друзей персонажа.
# Здесь мы можем рассмотреть работу очереди.
# ----------
# Breadth-first search using hash tables (dictionaries) and deques.
# Here we need to find a mango seller among the friends and the friends of friends of a character.
# Here we can see how deque works.


# Двусторонняя очередь - это тип структуры данных, похожий на стек вызовов:
# мы не можем обращаться к произвольным элементам двусторонней очереди.
# В двусторонней очереди поддерживается две операции: постановка в очередь и извлечение из очереди.
# Двусторонняя очередь позволяет добавлять или удалять элементы как с начала, так и с конца очереди.
# Чтобы создать двусторонние очереди нужно использовать контейнер в виде списка "deque" из модуля "collections".
# Ключевое слово "import" используется для импорта модулей.
# Ключевое слово "from" используется для импорта каких-то определенных разделов из модуля.
# ----------
# Deque is a data structure type similar to call stack:
# we can't choose the element that we want to access.
# Deque supports two operations: enqueue and dequeue.
# Deque allows us to add or remove elements from both the beginning and the end of a queue.
# To create deques, you need to use the list-like container "deque" from the module "collections".
# The keyword "import" is used to import modules.
# The keyword "from" is used to import certain sections from a module.
from collections import deque


# Создаем функцию "person_is_seller", которая принимает один входной параметр:
# переменная "char_name", содержащая имя персонажа, чтобы проверить, является ли этот персонаж продавцом манго или нет.
# Если имя персонажа заканчивается на букву "r", то функция "person_is_seller" возвращает "True",
# иначе эта функция возвращает "False".
# Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
# ----------
# Create the function "person_is_seller" that accepts one parameter:
# the variable "char_name" containing a name of a character to check if this character is a mango seller or not.
# If the name of a character ends with the letter "r", then the function "person_is_seller" returns "True",
# otherwise this function returns "False".
# The keyword "return" is to exit a function and return a value.
def person_is_seller(char_name):
    return char_name[-1] == 'r'


# Создаем словарь "char_graph", который представляет из себя граф персонажей и их ближайших друзей.
# С каждым ключом связано значение, которое является списком.
# Этот список является списком ближайших друзей персонажа, имя которого представлено в ключе.
# ----------
# Create the dictionary "char_graph", that is a graph of the characters and their closest friends.
# Each key has an associated value that is a list.
# This list is a list of the closest friends of a character whose name is represented in a key.
char_graph = {"Shepard": ["Garrus", "Liara", "Wrex"],
              "Garrus": ["Grunt"],
              "Liara": ["Grunt", "Shadow Broker"],
              "Wrex": ["Mordin", "Tali"],
              "Shadow Broker": [],
              "Grunt": [],
              "Mordin": [],
              "Tali": []}


# Создаем функцию "search_seller", которая принимает один входной параметр:
# переменная "char_name", содержащая имя персонажа, чтобы проверить,
# нет ли у этого персонажа в друзьях или в друзьях друзей продавца манго.
# ----------
# Create the function "search_seller" that accepts one parameter:
# the variable "char_name" containing a name of a character to check if this character has a mango seller
# among the friends and the friends of friends of this character.
def search_seller(char_name):
    # Создаем новую двустороннюю очередь "search_queue" при помощи метода "deque()".
    # ----------
    # Create the new deque "search_queue" by using the method "deque()".
    search_queue = deque()
    # Добавляем всех ближайших друзей персонажа "char_name" в двустороннюю очередь "search_queue".
    # ----------
    # Add all the closest friends of the character "char_name" to the deque "search_queue"
    search_queue += char_graph[char_name]
    # Создаем список "searched", в который мы добавляем тех персонажей, которых уже проверили.
    # Изначально этот список пустой.
    # ----------
    # Create the list "searched", to which we add those characters that we have already checked.
    # Initially this list is empty.
    searched = []
    # Создаем цикл while, который работает пока двусторонняя очередь "search_queue" не является пустой.
    # ----------
    # Create the while loop that works as long as the deque "search_queue" is not empty.
    while search_queue:
        # Из двусторонней очереди "search_queue" извлекается первый элемент.
        # Метод "popleft()" удаляет из очереди "search_queue" первый элемент и возвращает его переменной "person".
        # ----------
        # The first element is retrieved from the deque "search_queue".
        # The method "popleft()" removes the first element from the deque "search_queue"
        # and returns it to the variable "person".
        person = search_queue.popleft()
        # Если персонаж "person" не находится в списке "searched" и
        # ----------
        # If the character "person" is not in the list "searched" and
        if person not in searched:
            # если этот персонаж "person" яляется продавцом манго (здесь вызывается функция "person_is_seller"),
            # то выводится на экран сообщение о том, что этот персонаж "person" является продавцом манго.
            # Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
            # ----------
            # if this character "person" is a mango seller (here the function "person_is_seller" is called),
            # then the message stating that this "person" is a mango seller is displayed.
            # The function "print()" prints the specified message to the screen, or other standard output device.
            if person_is_seller(person):
                return print(person + " is a mango seller!")
            # Иначе, если этот персонаж "person" не является продавцом манго,
            # то все ближайшие друзья этого персонажа "person" добавляются в конец двусторонней очереди "search_queue".
            # ----------
            # Otherwise, if this character "person" is not a mango seller,
            # then all the closest friends of this character "person" are added to the end of the deque "search_queue".
            else:
                search_queue += char_graph[person]
                # А также этот персонаж "person" добавляется в список "searched",
                # чтобы избежать повторной проверки этого персонажа.
                # ----------
                # And also this character "person" is added to the list "searched"
                # to avoid re-checking this character.
                searched.append(person)
    # Если очередь "search_queue" оказывается пустой, то это означает, что среди персонажей нет продавца манго.
    # Выводится на экран сообщение о том, что среди персонажей нет продавца манго.
    # ----------
    # If the deque "search_queue" happens to be empty, it means there is no mango seller among the characters.
    # The message stating that there is no mango seller among the characters is displayed.
    return print("There is no mango seller among the characters")


# Попытаемся найти продавца манго среди друзей и друзей друзей персонажа Shepard.
# ----------
# Try to find a mango seller among the friends and the friends of friends of the character Shepard.
search_seller("Shepard")
