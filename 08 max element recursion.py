# Поиск наибольшего элемента используя рекурсию.
# ----------
# Finding the greatest element using recursion.


# Создаем функцию "find_max_one", которая принимает один входной параметр:
# список "list_one", содержащий элементы для поиска наибольшего из них.
# ----------
# Create the function "find_max_one" that accepts one parameter:
# the list "list_one" containing the elements to find the greatest one.
def find_max_one(list_one):
    # Если список "list_two" содержит 0 элементов, то функция "find_max_one" возвращает "None".
    # "None" означает nil (ничто) в Python. Используем, чтобы определять, что значения нет в списке.
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # ----------
    # If the list "list_one" contains 0 elements, then the function "find_max_one" returns "None".
    # "None" means nil (nothing) in Python. We use it to define that the number to find is not in the list.
    # The keyword "return" is to exit a function and return a value.
    if len(list_one) == 0:
        return None
    # Создаем базовый случай.
    # Базовый случай в рекурсивной функции - это часть кода функции, в которой описывается
    # условие прекращения работы функции в целях предотвращения зацикливания.
    # Если одна из вызванных рекурсивно копий функции "find_max_one" принимает в качестве параметра список,
    # содержащий 1 элемент, то мы выходим из этой копии функции "find_max_one" и возвращаем первый элемент этого списка
    # предыдущей копии функции "find_max_one" в стеке вызовов, поскольку если список содержит только один элемент,
    # то этот элемент будет наибольшим.
    # Если изначально вызывается функция "find_max_one", которая принимает в качестве параметра список,
    # содержащий 1 элемент, то функция "find_max_one" сразу возвращает первый элемент этого списка,
    # поскольку если список содержит только один элемент, то этот элемент будет наибольшим.
    # ----------
    # Create the base case.
    # The base case in a recursive function is a part of the function code that describes
    # the condition for the termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "find_max_one" takes the list containing 1 element
    # as a parameter, then we exit this recursively called copy of the function "find_max_one"
    # and it returns the first element of this list to the previous copy of the function "find_max_one"
    # in the call stack, since if a list contains only 1 element, then this element is the greatest one.
    # If the function "find_max_one" is initially called with the list containing 1 element as a parameter,
    # then the function "find_max_one" immediately returns the first element of this list,
    # since if a list contains only 1 element, then this element is the greatest one.
    if len(list_one) == 1:
        return list_one[0]
    # Создаем рекурсивный случай.
    # Рекурсивный случай в рекурсивной функции - это часть кода функции, в которой функция вызывает сама себя
    # в целях выполнения какой-либо задачи.
    # Если первый элемент больше второго элемента в списке "list_one", то этот второй элемент удаляется
    # при помощи ключевого слова "del" и рекурсивно вызывается новая копия функции "find_max_one"
    # с этим уменьшенным списком "list_one" в качестве параметра.
    # Когда рекурсивно вызывается копия функции "find_max_one", которая принимает в качестве параметра список,
    # содержащий 1 элемент, то срабатывает базовый случай.
    # Копии функции "find_max_one" в стеке вызовов поочередно завершают свою работу
    # и возвращают свои рассчитанные значения предыдущим рекурсивно вызванным копиям функции "find_max_one" до тех пор,
    # пока не завершит работу самая первая вызванная функция "find_max_one".
    # ----------
    # Create the recursive case.
    # The recursive case in a recursive function is a part of the function code
    # in which the function calls itself in order to perform a task.
    # If the first element is bigger than the second element in the list "list_one", then this second element is deleted
    # using the keyword "del" and the new copy of the function "find_max_one" is recursively called
    # with this reduced list "list_one" as a parameter.
    # When a copy of the function "find_max_one" is recursively called with the list containing 1 element
    # as a parameter, then the base case is triggered.
    # The copies of the function "find_max_one" in the call stack terminate one by one and return
    # their calculated values to the previous recursively called copies of the function "find_max_one"
    # until the very first called function "find_max_one" stops its work.
    if list_one[0] > list_one[1]:
        del list_one[1]
        return find_max_one(list_one)
    # Иначе если первый элемент меньше второго элемента в списке "list_one", то рекурсивно вызывается
    # новая копия функции "find_max_one" со списком "list_one", за исключением первого элемента, в качестве параметра.
    # ----------
    # Otherwise, if the first element is less than the second element in the list "list_one",
    # then the new copy of the function "find_max_one" is recursively called with the list "list_one"
    # except for the first element as a parameter.
    else:
        return find_max_one(list_one[1:])


# Создаем 2 списка и попытаемся найти в них наибольшие элементы.
# Список "my_list1" содержит несколько чисел, а список "my_list2" является пустым.
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Create the 2 lists and try to find the greatest elements in these lists.
# The list "my_list1" contains several numbers, but the list "my_list2" is empty.
# The function "print()" prints the specified message to the screen, or other standard output device.
my_list1 = [2, 0, 6, 9, 7, 7]
my_list2 = []
print(find_max_one(my_list1))
print(find_max_one(my_list2))


# Давайте создадим еще один вариант функции для поиска наибольшего элемента.
# Здесь мы создаем другой рекурсивный случай.
# Создаем функцию "find_max_two", которая принимает один входной параметр:
# список "list_two", содержащий элементы для поиска наибольшего из них.
# ----------
# Let's create another variation of the function to find the greatest element.
# Here we are creating another recursive case.
# Create the function "find_max_two" that accepts one parameter:
# the list "list_two" containing the elements to find the greatest one.
def find_max_two(list_two):
    # Если список содержит 0 элементов, то функция "find_max_two" возвращает "None".
    # "None" означает nil (ничто) в Python. Используем, чтобы определять, что значения нет в списке.
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # ----------
    # If the list "list_two" contains 0 elements, then the function "find_max_two" returns "None".
    # "None" means nil (nothing) in Python. We use it to define that the number to find is not in the list.
    # The keyword "return" is to exit a function and return a value.
    if len(list_two) == 0:
        return None
    # Создаем базовый случай.
    # Если одна из вызванных рекурсивно копий функции "find_max_two" принимает в качестве параметра список,
    # содержащий 1 элемент, то мы выходим из этой копии функции "find_max_two" и возвращаем первый элемент этого списка
    # предыдущей копии функции "find_max_two" в стеке вызовов, поскольку если список содержит только один элемент,
    # то этот элемент будет наибольшим.
    # Если изначально вызывается функция "find_max_two", которая принимает в качестве параметра список,
    # содержащий 1 элемент, то функция "find_max_two" сразу возвращает первый элемент этого списка,
    # поскольку если список содержит только один элемент, то этот элемент будет наибольшим.
    # ----------
    # Create the base case.
    # If one of the recursively called copies of the function "find_max_two" takes the list containing 1 element
    # as a parameter, then we exit this recursively called copy of the function "find_max_two"
    # and it returns the first element of this list to the previous copy of the function "find_max_two"
    # in the call stack, since if a list contains only 1 element, then this element is the greatest one.
    # If the function "find_max_two" is initially called with the list containing 1 element as a parameter,
    # then the function "find_max_two" immediately returns the first element of this list,
    # since if a list contains only 1 element, then this element is the greatest one.
    if len(list_two) == 1:
        return list_two[0]
    # Создаем рекурсивный случай.
    # Рекурсивно вызывается новая копия функции "find_max_two" со списком "list_two", за исключением первого элемента,
    # в качестве параметра, причем результат работы этой рекурсивно вызванной копии функции "find_max_two" хранится
    # в локальной переменной "sub_max".
    # Любая копия функции "find_max_two" возвращает результат на основе следующего условия:
    # она возвращает первый элемент списка "list_two", если этот первый элемент больше
    # значения локальной переменной "sub_max", иначе возвращается эта локальная переменная "sub_max".
    # Когда рекурсивно вызывается копия функции "find_max_two", которая принимает в качестве параметра список,
    # содержащий 1 элемент, то срабатывает базовый случай.
    # Копии функции "find_max_two" в стеке вызовов поочередно завершают свою работу
    # и возвращают свои рассчитанные значения предыдущим рекурсивно вызванным копиям функции "find_max_two" до тех пор,
    # пока не завершит работу самая первая вызванная функция "find_max_two".
    # ----------
    # Create the recursive case.
    # The new copy of the function "find_max_two" is recursively called with the list "list_two"
    # except for the first element as a parameter,
    # and the result of this recursively called copy of the function "find_max_two" is stored
    # in the local variable "sub_max".
    # Any copy of the function "find_max_two" returns a result based on the following condition:
    # it returns the first element of the list "list_two" if this first element is bigger than the value of
    # the local variable "sub_max", otherwise this local variable "sub_max" is returned.
    # When a copy of the function "find_max_two" is recursively called with the list containing 1 element
    # as a parameter, then the base case is triggered.
    # The copies of the function "find_max_two" in the call stack terminate one by one and return
    # their calculated values to the previous recursively called copies of the function "find_max_two"
    # until the very first called function "find_max_two" exits.
    else:
        sub_max = find_max_two(list_two[1:])
        return list_two[0] if list_two[0] > sub_max else sub_max


# Попытаемся найти наибольшие элементы в списках "my_list1" и "my_list2", используя функцию "find_max_two".
# ----------
# Try to find the greatest elements in the lists "my_list1" and "my_list2" using the function "find_max_two".
print(find_max_two(my_list1))
print(find_max_two(my_list2))
