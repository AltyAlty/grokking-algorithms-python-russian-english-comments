# Бинарный поиск. [O(log n)]
# ----------
# Binary Search. [O(log n)]


# Создаем функцию "binary_search", которая принимает два входных параметра:
# список "search_list" и число для поиска "number".
# Эта функция возвращает индекс элемента, который является числом для поиска "number".
# ----------
# Create the function "binary_search" that accepts two parameters: the number to find "number"
# and the list "search_list" that contains this number.
# This function returns the index of the element that is the number to find "number".
def binary_search(search_list, number):
    # В переменных "low" и "high" хранятся границы области поиска в списке "search_list".
    # Функция "len()" возвращает количество элементов в списке.
    # ----------
    # The variables "low" and "high" store the bounds of the search area in the list "search_list".
    # The function "len()" returns the number of elements in a list.
    low = 0
    high = len(search_list) - 1
    # Создаем цикл while, который работает пока нижняя граница области поиска меньше или равна
    # верхней границе этой области поиска.
    # После выполнения одного из условий, область поиска уменьшается и цикл while продолжает свою работу сначала.
    # ----------
    # Create the while loop that works as long as
    # the lower bound of the search area is equal to or less than the upper bound of the search area.
    # If one of the conditions below is true, then the search area decreases
    # and the while loop continues its work from the beginning.
    while low <= high:
        # Находим средний элемент списка "search_list". Переменная "mid" - индекс этого среднего элемента.
        # Переменная "guess" - значение по этому индексу. Значение переменной "mid" округляется в меньшую сторону.
        # ----------
        # Find a middle element of the list "search_list". The variable "mid" is the index of this middle element.
        # The variable "guess" is the value of this middle element. The value of the variable "mid" is rounded down.
        mid = (low + high) // 2
        guess = search_list[mid]
        # Если значение среднего элемента списка "search_list" равно числу, которое мы ищем,
        # то функция "binary_search" возвращает индекс этого среднего элемента.
        # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
        # ----------
        # If the value of the middle element of the list "search_list" is equal to the number to find,
        # then the function "binary_search" returns the index of this middle element.
        # The keyword "return" is to exit a function and return a value.
        if guess == number:
            return mid
        # Если значение среднего элемента списка "search_list" больше числа, которого мы ищем,
        # то верхняя граница области поиска становится равной на одну позицию меньше,
        # чем индекс этого среднего элемента.
        # ----------
        # If the value of the middle element of the list "search_list" is greater than the number to find,
        # then the upper bound of the search area is one position less
        # than the index of this middle element.
        if guess > number:
            high = mid - 1
        # Иначе если значение среднего элемента списка "search_list" меньше числа, которого мы ищем,
        # то нижняя граница области поиска становится равной на одну позицию больше,
        # чем индекс этого среднего элемента.
        # ----------
        # Otherwise, if the value of the middle element of the list "search_list" is less than the number to find,
        # then the lower bound of the search area is one position greater
        # than the index of this middle element.
        else:
            low = mid + 1
    # Если число для поиска отсутствует в списке "search_list" (условие "low <= high" не является верным,
    # этот факт означает, что область поиска пуста), то функция "binary_search" возвращает "None".
    # "None" означает nil (ничто) в Python. Мы используем это, чтобы определять, что числа нет в списке.
    # ----------
    # If the number to find is not in the list "search_list" (the condition "low <= high" is false,
    # this fact means that the search area is empty), then the function "binary_search" returns "None".
    # "None" means nil (nothing) in Python. We use it to define that the number to find is not in the list.
    return None


# Создаем список чисел "my_list".
# ----------
# Create the list of numbers "my_list".
my_list = [1, 3, 5, 7, 9]


# Пытаемся найти индекс элемента, который находится в списке "my_list".
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Try to find the index of the element that is in the list "my_list".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(binary_search(my_list, 7))


# Пытаемся найти индекс элемента, который не находится в списке "my_list".
# ----------
# Try to find the index of the element that is not in the list "my_list".
print(binary_search(my_list, 8))
