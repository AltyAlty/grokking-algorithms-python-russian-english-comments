# Бинарный поиск.
# ----------
# Binary Search.


# Создаем функцию "binary_search", которая принимает два входных параметра:
# список "search_list" и число для поиска "number". Эта функция возвращает индекс элемента.
# ----------
# Creating the function "binary_search" that accepts two parameters - the number to find "number"
# and the list "search_list" that contains this number.
# This function returns the index of the element.
def binary_search(search_list, number):
    # В переменных "low" и "high" хранятся границы области поиска.
    # ----------
    # The variables "low" and "high" store the bounds of the search area.
    low = 0
    high = len(search_list) - 1
    # Создаем цикл while, который работает пока нижняя граница списка меньше или равна верхней границе этого списка.
    # После выполнения одного из условий, область поиска уменьшается и цикл while начинает работу сначала.
    # ----------
    # Creating the while loop that works as long as
    # the lower bound of the list is equal or less than the upper bound of the list.
    # If one of the conditions below is true, the search area decreases and the while loop starts over.
    while low <= high:
        # Находим средний элемент списка. Переменная "mid" - индекс среднего элемента.
        # Переменная "guess" - значение по этому индексу. Индекс среднего элемента округляется в меньшую сторону.
        # ----------
        # Trying to find the middle element of the list. The variable "mid" is the index of the middle element.
        # The variable "guess" is the value of the middle element. The value of the variable "mid" is rounded down.
        mid = (low + high) // 2
        guess = search_list[mid]
        # Если значение среднего элемента списка равно числу, которое мы ищем,
        # то функция "binary_search" возвращает индекс этого среднего элемента списка.
        # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
        # ----------
        # If the value of the middle element of the list is equal the number that we try to find
        # then the function "binary_search" returns the index of this middle element of the list.
        # The keyword "return" is to exit a function and return a value.
        if guess == number:
            return mid
        # Если значение среднего элемента списка больше числа, которого мы ищем,
        # то верхняя граница области поиска становится равной на одну позицию меньше,
        # чем индекс этого среднего элемента списка.
        # ----------
        # If the value of the middle element of the list is more than the number that we try to find
        # then the upper bound of the search area is one position less
        # than the index of this middle element of the list.
        if guess > number:
            high = mid - 1
        # Иначе если значение среднего элемента списка меньше числа, которого мы ищем,
        # то нижняя граница области поиска становится равной на одну позицию больше,
        # чем индекс этого среднего элемента списка.
        # ----------
        # Otherwise, if the value of the middle element of the list is less than the number that we try to find
        # then the lower bound of the search area is one position more
        # than the index of this middle element of the list.
        else:
            low = mid + 1
    # Если число для поиска отсуствует в списке (условие "low <= high" не является верным),
    # то функция "binary_search" возвращает значение "None".
    # "None" означает nil (ничто) в Python. Используем, чтобы определять, что значения нет в списке.
    # ----------
    # If the number to find is not in the list (condition "low <= high" is false)
    # then the function "binary_search" returns value "None".
    # "None" means nil (nothing) in Python. We use it to define than the number to find is not in the list.
    return None


# Создаем список чисел "my_list".
# ----------
# Creating the list of numbers "my_list".
my_list = [1, 3, 5, 7, 9]

# Пытаемся найти индекс элемента, который находится в списке "my_list".
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Trying to find the index of the element that is in the list "my_list".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(binary_search(my_list, 7))

# Пытаемся найти индекс элемента, который не находится в списке "my_list".
# ----------
# Trying to find the index of the element that is not in the list "my_list".
print(binary_search(my_list, 8))
