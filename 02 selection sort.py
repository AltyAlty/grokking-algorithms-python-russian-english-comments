# Сортировка выбором.
# Здесь мы создаем две функции:
# первая функция находит наименьший элемент в списке,
# а вторая функция сортирует список путем сравнения каждого элемента списка с наименьшим элементом списка.
# ----------
# Selection sort.
# Here we create two functions:
# the first function finds the smallest element in a list,
# and the second function sorts the list by comparing each element in the list with the smallest element in the list.


# Создаем функцию "find_smallest", которая принимает один входной параметр:
# список "list_to_sort", который содержит числа. Эта функция возвращает индекс наименьшего элемента в списке.
# ----------
# Create the function "find_smallest" that accepts one parameter: the list "list_to_sort" that contains the numbers.
# This function returns the index of the smallest number in the list.
def find_smallest(list_to_sort):
    # Переменная "smallest" используется для хранения наименьшего элемента в списке.
    # Изначально переменная "smallest" хранит самый первый элемент в списке - элемент под индексом "0".
    # ----------
    # The variable "smallest" is used to store the smallest element in the list.
    # Initially the variable "smallest" stores the very first element in the list - the element at index "0".
    smallest = list_to_sort[0]
    # Переменная "smallest_index" используется для хранения индекса наименьшего элемента в списке.
    # Изначально переменная "smallest_index" хранит индекс самого первого элемента в списке - "0".
    # ----------
    # The variable "smallest_index" is used to store the index of the smallest element in the list.
    # Initially the variable "smallest_index" stores the index of the very first element in the list - "0".
    smallest_index = 0
    # Создаем цикл for, в котором перебираем все элементы списка, кроме элемента под индексом "0",
    # и сравниваем эти элементы с элементом под индексом "0".
    # Функция "range()" возвращает последовательность чисел, за исключением последнего число.
    # Функция "len()" возвращает количество элементов в списке.
    # ----------
    # Create the for loop in which we iterate over all the elements of the list, except for the element at index "0",
    # and comparing these elements with the element at index "0".
    # The function "range()" returns a sequence of numbers excluding the last number.
    # The function "len()" returns the number of elements in a list.
    for i in range(1, len(list_to_sort)):
        # Если находим элемент, который меньше элемента с индексом "0",
        # то этот элемент становится новым наименьшим элементом в списке.
        # Остальные элемента списка сравниваются с этим новым наименьшим элементом в списке.
        # ----------
        # If we find the element that is less than the element at index "0",
        # then this element becomes the new smallest element in the list.
        # The rest elements of the list are compared with this new smallest element of the list.
        if list_to_sort[i] < smallest:
            smallest_index = i
            smallest = list_to_sort[i]
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # В результате работы цикла for функция "find_smallest" возвращает индекс наименьшего элемента в списке.
    # ----------
    # The keyword "return" is to exit a function and return a value.
    # As a result of the for loop, the function "find_smallest" returns the index of the smallest number in the list.
    return smallest_index


# Создаем функцию "selection_sort", которая принимает один входной параметр:
# список "list_to_sort", который содержит числа. Эта функция возвращает отсортированный список по возрастанию.
# ----------
# Create the function "selection_sort" that accepts one parameter: the list "search_list" that contains the numbers.
# This function returns the sorted list in ascending order.
def selection_sort(list_to_sort):
    # Переменная "new_list" используется для хранения отсортированного списка по возрастанию.
    # Изначально переменная "new_list" содержит пустой список.
    # ----------
    # The variable "new_list" is used to store the sorted list in ascending order.
    # Initially the variable "new_list" contains an empty list.
    new_list = []
    # Создаем цикл for, в котором перебираем все элементы списка.
    # ----------
    # Create the for loop in which we iterate over all the elements of the list.
    for i in range(len(list_to_sort)):
        # Вызываем функцию "find_smallest", чтобы найти индекс наименьшего элемента в списке.
        # Переменная "smallest" хранит этот индекс наименьшего элемента в списке.
        # ----------
        # Call the function "find_smallest" to find the index of the smallest element in the list.
        # The variable "smallest" stores this index of the smallest element in the list.
        smallest = find_smallest(list_to_sort)
        # Убираем элемент с индексом "smallest" из списка "list_to_sort" при помощи метода "pop".
        # Также метод "pop" возвращает убранный элемент.
        # Добавляем в конец списка "new_list" полученный от метода "pop" элемент при помощи метода "append".
        # Затем цикл for начинает работа сначала с уменьшенным списком "list_to_sort".
        # ----------
        # Remove the element at index "smallest" from the list "list_to_sort" using the method "pop".
        # Also the method "pop" returns the removed element.
        # Add the element received from the method "pop" to the end of the list "new_list" using the method "append".
        # Then the for loop starts over with the reduced list "list_to_sort".
        new_list.append(list_to_sort.pop(smallest))
    # В результате работы цикла for функция "selection_sort" возвращает переменную "new_list",
    # которая хранит отсортированный список по возрастанию.
    # ----------
    # As a result of the for loop, the function "selection_sort" returns the variable "new_list"
    # which stores the sorted list in ascending order.
    return new_list


# Пытаемся отсортировать список [5, 3, 6, 2, 10] по возрастанию.
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Try to sort the list [5, 3, 6, 2, 10] in ascending order.
# The function "print()" prints the specified message to the screen, or other standard output device.
print(selection_sort([5, 3, 6, 2, 10]))
