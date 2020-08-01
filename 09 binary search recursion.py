# Бинарный поиск используя рекурсию.
# ----------
# Binary Search using recursion.


# Создаем функцию "binary_search", которая принимает 4 входных параметра:
# список "search_list", переменные "low" и "high", которые хранят границы области поиска в списке "search_list",
# и число для поиска "element".
# Эта функция возвращает индекс элемента.
# ----------
# Create the function "binary_search" that accepts 4 parameters:
# the number to find "element", the list "search_list" that contains this number, and the variables "low" and "high"
# that store the bounds of the search area in the list "search_list".
# This function returns the index of the element.
def binary_search(search_list, low, high, element):
    # Создаем локальную переменную "upper_bound_error_list", которую мы используем для проверки указанных
    # границ списка: не превышает ли указанная верхняя граница действительную верхнюю границу списка "search_list"
    # или не является ли указанная нижняя граница меньше действительной нижней границы списка "search_list".
    # ----------
    #
    upper_bound_error_list = []
    # В блоке try, используя цикл for, пытаемся перебрать все элементы списка "search_list"
    # и поместить их в список "upper_bound_error_list", при помощи метода "append".
    # ----------
    #
    try:
        for i in range(low, high+1):
            upper_bound_error_list.append(search_list[i])
    # В блоке except пытаемся перехватить ошибку "IndexError", в случае если
    # мы попытались поместить в список "upper_bound_error_list" элемент,
    # который имеет индекс больший максимального индекса в списке "search_list"
    # или который имеет индекс меньший минимального индекса в списке "search_list".
    # Если мы успешно перехватываем ошибку "IndexError", то выводится сообщение об ошибке и
    # программа продолжает свою работу.
    # Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
    # ----------
    #
    # The function "print()" prints the specified message to the screen, or other standard output device.
    except IndexError:
        return print("Указанная верхняя граница превышает действительную верхнюю границу списка "
                     "или указанная нижняя граница меньше действительной нижней границы списка \n"
                     "----------")
    # Если указанная нижняя граница меньше или равна указанной верхней границе,
    # а также эта нижняя граница больше или равна 0,
    # то находим индекс среднего элемента списка "search_list".
    # Переменная "mid" содержит этот индекс среднего элемента списка "search_list".
    # Индекс среднего элемента списка "search_list" округляется в меньшую сторону.
    # ----------
    #
    if high >= low >= 0:
        mid = low + (high - low) // 2
        # Создаем базовый случай.
        # Базовый случай в рекурсивной функции - это часть кода функции, в которой описывается
        # условие прекращения работы функции в целях предотвращения зацикливания.
        # Если значение среднего элемента списка "search_list" равно числу, которое мы ищем,
        # или же
        # если список "search_list" содержит 1 элемент и этот элемент равен числу, которое мы ищем,
        # то функция "binary_search" возвращает индекс этого среднего элемента списка "search_list".
        # ----------
        # Create the base case.
        # The base case in a recursive function is a part of the function code that describes
        # the condition for the termination of the function in order to prevent loops.
        #
        if search_list[mid] == element:
            return print("Искомый элемент находится под индексом %d \n"
                         "----------" % mid)

        # Иначе если нужный элемент меньше того, что находится в середине списка,
        # тогда вызываем рекурсивно функцию, как если бы мы искали только в левой части списка,
        # то есть от начала до элемента в середине, не включая его.
        # При этом мы не используем срезы, а только изменяем переменные,
        # обозначающие верхнюю и нижнюю границы списка для поиска.

        # Создаем рекурсивный случай.
        # Рекурсивный случай в рекурсивной функции - это часть кода функции, в которой функция вызывает сама себя
        # в целях выполнения какой-либо задачи.
        # Если значение среднего элемента списка больше числа, которого мы ищем,
        # то рекурсивно вызывается копия функции "binary_search", в которой
        # верхняя граница области поиска становится равной на одну позицию меньше,
        # чем индекс этого среднего элемента списка.
        # ----------
        # Create the recursive case.
        # The recursive case in a recursive function is a part of the function code
        # in which the function calls itself in order to perform a task.
        #
        elif search_list[mid] > element:
            return binary_search(search_list, low, mid - 1, element)
        # Иначе если значение среднего элемента списка меньше числа, которого мы ищем,
        # то рекурсивно вызывается копия функции "binary_search", в которой
        # нижняя граница области поиска становится равной на одну позицию больше,
        # чем индекс этого среднего элемента списка.
        # ----------
        #
        else:
            return binary_search(search_list, mid + 1, high, element)

    # Иначе если заданы неверно границы списка
    # или не сработало ни одного из трех условий для поиска (то есть необходимое значение отсутствует в списке),
    # то выводим соответствующее сообщение об ошибке.

    # Если число для поиска отсутствует в списке (условие "high >= low" не является верным, этот факт означает,
    # что область поиска пуста),
    # или если указанная нижняя граница меньше действительной нижней границы списка,
    # или если указанная верхняя граница превышает действительную верхнюю границу списка, то
    # то функция "binary_search" выводит соответствующее информационное сообщение.
    # ----------
    #
    else:
        return print("Искомого элемента нет в списке или "
                     "указанная верхняя граница превышает действительную верхнюю границу списка "
                     "или указанная нижняя граница меньше действительной нижней границы списка \n"
                     "----------")

    # В этой функции "binary_search" не учтено условие, когда указанные границы списка образуют список, который
    # входит в список "search_list", но является меньше его.
    # Например, "search_list" = [1, 2, 3, 4], low = 1, high = 2, то эти указанные границы образуют список [2, 3] и
    # программа все равно попытается найти число "element".
    # ----------
    #


# Создаем список чисел "my_list".
# ----------
# Create the list of numbers "my_list".
my_list = [0, 2, 6, 7, 7, 9]


# Создаем переменную "x", хранящяя число, которое находится в списке "my_list".
# ----------
# Create the variable "x" to store the number that is in the list "my_list".
x = 6


# Создаем переменную "y", хранящяя число, которое не находится в списке "my_list".
# ----------
# Create the variable "y" to store the number that is not in the list "my_list".
y = 4


# Попытаемся вызвать функцию "binary_search" c разными наборами входных параметрами.
# ----------
# Try to call the function "binary_search" with different sets of parameters.

# Все параметры указаны верно.
# ----------
# All specified parameters are correct.
binary_search(my_list, 0, len(my_list) - 1, x)

# Нижняя граница указана неверно.
# ----------
# The specified lower bound is not correct.
binary_search(my_list, -1, len(my_list) - 1, x)

# Нижняя граница указана неверно.
# ----------
# The specified lower bound is not correct.
binary_search(my_list, -7, len(my_list) - 1, x)

# Верхняя граница указана неверно.
# ----------
# The specified upper bound is not correct.
binary_search(my_list, 0, 6, x)

# Верхняя граница указана неверно.
# ----------
# The specified upper bound is not correct.
binary_search(my_list, 0, -1, x)

# Верхняя граница указана неверно.
# ----------
# The specified upper bound is not correct.
binary_search(my_list, 0, -8, x)

# Нижняя граница больше верхней границы.
# ----------
# The specified lower bound is more than the specified upper bound.
binary_search(my_list, 3, 2, x)

# Число, которое нужно найти, указано неверно.
# ----------
# The specified number to find is not correct.
binary_search(my_list, 0, len(my_list) - 1, y)

# Указанные границы образуют список, который входит в список "search_list", но является меньше его.
# ----------
# The specified bounds form the list that is smaller than the list "search_list".
binary_search(my_list, 1, 4, x)
