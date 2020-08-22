# Бинарный поиск, используя рекурсию. [O(log n)]
# ----------
# Binary search using recursion. [O(log n)]


# Создаем функцию "binary_search", которая принимает 4 входных параметра:
# список "search_list", переменные "low" и "high", которые хранят границы области поиска в списке "search_list",
# и число для поиска "element".
# Эта функция возвращает индекс элемента, который является числом для поиска "number".
# ----------
# Create the function "binary_search" that accepts 4 parameters:
# the number to find "element", the list "search_list" that contains this number, and the variables "low" and "high"
# that store the bounds of the search area in the list "search_list".
# This function returns the index of the element which is the number to find "number".
def binary_search(search_list, low, high, element):
    # Создаем локальную переменную "upper_bound_error_list", которую мы используем для проверки указанных
    # границ области поиска:
    # 1. не превышает ли указанная верхняя граница действительную верхнюю границу списка "search_list";
    # 2. не является ли указанная нижняя граница меньше действительной нижней границы списка "search_list".
    # ----------
    # Create the variable "upper_bound_error_list" that we use to check the specified bounds of the search area:
    # 1. whether the specified upper bound is greater than the actual upper bound of the list "search_list" or not;
    # 2. whether the specified lower bound is less than the actual lower bound of the list "search_list" or not.
    upper_bound_error_list = []
    # В блоке try, используя цикл for, пытаемся перебрать все элементы списка "search_list"
    # и поместить их в список "upper_bound_error_list", при помощи метода "append".
    # Функция "range()" возвращает последовательность чисел, за исключением последнего число.
    # ----------
    # In the try block, using a for loop, we try to iterate over all the elements of the list "search_list"
    # and place them in the list "upper_bound_error_list" using the method "append".
    # The function "range()" returns a sequence of numbers excluding the last number.
    try:
        for i in range(low, high+1):
            upper_bound_error_list.append(search_list[i])
    # В блоке except пытаемся перехватить ошибку "IndexError", в случае если
    # мы пытаемся поместить в список "upper_bound_error_list" элемент,
    # который имеет индекс больший максимального индекса в списке "search_list"
    # или который имеет индекс меньший минимального индекса в списке "search_list".
    # Если мы успешно перехватываем ошибку "IndexError", то выводится сообщение об ошибке и
    # программа продолжает свою работу.
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
    # ----------
    # In the except block we try to catch th error "IndexError",
    # if we try to place in the list "upper_bound_error_list" the element, that has the index greater
    # than the maximum index of the list "search_list",
    # or that has the index less than the minimum index of the list "search_list".
    # If we successfully catch the error "IndexError", then the error message is displayed
    # and the program continues its work.
    # The keyword "return" is to exit a function and return a value.
    # The function "print()" prints the specified message to the screen, or other standard output device.
    except IndexError:
        return print("The specified upper bound is greater than the actual upper bound of the list "
                     "or the specified lower bound is less than the actual lower bound of the list \n"
                     "----------")
    # Если указанная нижняя граница меньше или равна указанной верхней границе,
    # а также эта нижняя граница больше или равна 0,
    # то находим индекс среднего элемента списка "search_list".
    # Переменная "mid" хранит этот индекс среднего элемента.
    # Значение переменной "mid" округляется в меньшую сторону.
    # ----------
    # if the specified lower bound is less than or equal to the specified upper bound
    # and this lower bound is greater than or equal to 0,
    # then we find the index of the middle element of the list "search_list".
    # The variable "mid" stores this index of the middle element.
    # The value of the variable "mid" is rounded down.
    if high >= low >= 0:
        mid = low + (high - low) // 2
        # Создаем базовый случай.
        # Базовый случай в рекурсивной функции - это часть функции, в которой описывается
        # условие прекращения работы функции в целях предотвращения зацикливания.
        # Если значение среднего элемента списка "search_list" равно числу, которое мы ищем,
        # или же если список "search_list" содержит 1 элемент и этот элемент равен числу, которое мы ищем,
        # то функция "binary_search" возвращает индекс этого среднего элемента.
        # ----------
        # Create the base case.
        # Base case in a recursive function is a part of a function that describes
        # a condition for termination of the function in order to prevent loops.
        # If the value of the middle element of the list "search_list" is equal to the number to find,
        # or if the list "search_list" contains 1 element and this element is equal to the number to find,
        # then the function "binary_search" returns the index of this middle element.
        if search_list[mid] == element:
            return print("The element we are looking for is at index %d \n"
                         "----------" % mid)
        # Создаем рекурсивный случай.
        # Рекурсивный случай в рекурсивной функции - это часть функции, в которой функция вызывает сама себя
        # в целях выполнения какой-либо задачи.
        # Если значение среднего элемента списка "search_list" больше числа, которого мы ищем,
        # то рекурсивно вызывается новая копия функции "binary_search", в которой
        # верхняя граница области поиска становится равной на одну позицию меньше,
        # чем индекс этого среднего элемента.
        # ----------
        # Create the recursive case.
        # Recursive case in a recursive function is a part of a function
        # in which the function calls itself in order to perform some task.
        # If the value of the middle element of the list "search_list" is greater than the number to find,
        # then a new copy of the function "binary_search" is recursively called,
        # in which the upper bound of the search area is one position less
        # than the index of this middle element.
        elif search_list[mid] > element:
            return binary_search(search_list, low, mid - 1, element)
        # Иначе если значение среднего элемента списка "search_list" меньше числа, которого мы ищем,
        # то рекурсивно вызывается новая копия функции "binary_search", в которой
        # нижняя граница области поиска становится равной на одну позицию больше,
        # чем индекс этого среднего элемента.
        # ----------
        # Otherwise, if the value of the middle element of the list "search_list" is less than the number to find,
        # then a new copy of the function "binary_search" is recursively called,
        # in which the lower bound of the search area is one position greater
        # than the index of this middle element.
        else:
            return binary_search(search_list, mid + 1, high, element)
    # Если число для поиска отсутствует в списке "search_list" (условие "high >= low" не является верным,
    # этот факт означает, что область поиска пуста),
    # или если указанная нижняя граница меньше действительной нижней границы списка "search_list",
    # или если указанная верхняя граница превышает действительную верхнюю границу списка "search_list",
    # то функция "binary_search" выводит соответствующее сообщение об ошибке.
    # ----------
    # If the number to find is not in the list "search_list" (the condition "high >= low" is false, this fact means
    # that the search area is empty),
    # or if the specified lower bound is less than the actual lower bound of the list "search_list",
    # or if the specified upper bound is greater than the actual upper bound of the list "search_list",
    # then the function "binary_search" displays the corresponding error message.
    else:
        return print("The element we are looking for is not in the list or "
                     "the specified upper bound is greater than the actual upper bound of the list "
                     "or the specified lower bound is less than the actual lower bound of the list \n"
                     "----------")
    # В этой функции "binary_search" не учтено условие, когда указанные границы области поиска образуют список, который
    # входит в список "search_list", но является меньше списка "search_list".
    # Например, если "search_list" = [1, 2, 3, 4], "low" = 1, "high" = 2, "element" = 4,
    # то эти указанные границы образуют список [2, 3] и программа все равно попытается найти число "element".
    # ----------
    # This function "binary_search" does not take into account the condition
    # when the specified bounds of the search area form the list that is included in the list "search_list",
    # but is less than the list "search_list".
    # For example, if "search_list" = [1, 2, 3, 4], "low" = 1, "high" = 2, "element" = 4,
    # then these specified bounds form the list [2, 3] and the program still tries to find the number "element".


# Создаем список чисел "my_list".
# ----------
# Create the list of numbers "my_list".
my_list = [0, 2, 6, 7, 7, 9]


# Создаем переменную "x", хранящую число, которое находится в списке "my_list".
# ----------
# Create the variable "x" to store the number that is in the list "my_list".
x = 6


# Создаем переменную "y", хранящую число, которое не находится в списке "my_list".
# ----------
# Create the variable "y" to store the number that is not in the list "my_list".
y = 4


# Попытаемся вызвать функцию "binary_search" c разными наборами входных параметрами.
# ----------
# Try to call the function "binary_search" with different sets of parameters.


# Все параметры указаны верно.
# Функция "len()" возвращает количество элементов в списке.
# ----------
# All the specified parameters are correct.
# The function "len()" returns the number of elements in a list.
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


# Указанная нижняя граница больше указанной верхней границы.
# ----------
# The specified lower bound is greater than the specified upper bound.
binary_search(my_list, 3, 2, x)


# Число, которое нужно найти, указано неверно.
# ----------
# The specified number to find is not correct.
binary_search(my_list, 0, len(my_list) - 1, y)


# Указанные границы образуют список,
# который входит в список "search_list", но является меньше списка "search_list".
# ----------
# The specified bounds form the list
# that is included in the list "search_list", but is less than the list "search_list".
binary_search(my_list, 1, 4, x)
