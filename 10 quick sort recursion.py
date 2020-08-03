# Быстрая сортировка используя рекурсию.
# ----------
# Quick sort using recursion.


# Создаем функцию "quick_sort", которая принимает один входной параметр:
# список "list_to_sort", который содержит числа. Эта функция возвращает отсортированный список по возрастанию.
# ----------
# Create the function "quick_sort" that accepts one parameter: the list "list_to_sort" that contains the numbers.
# This function returns the sorted list in ascending order.
def quick_sort(list_to_sort):
    # Создаем базовый случай.
    # Базовый случай в рекурсивной функции - это часть кода функции, в которой описывается
    # условие прекращения работы функции в целях предотвращения зацикливания.
    # Если одна из вызванных рекурсивно копий функции "quick_sort" принимает в качестве параметра список,
    # содержащий 1 или 0 элементов, то мы выходим из этой копии функции "quick_sort" и возвращаем этот список
    # предыдущей копии функции "quick_sort" в стеке вызовов, поскольку если список содержит 1 или 0 элементов,
    # то он уже отсортирован по возрастанию.
    # Если изначально вызывается функция "quick_sort", которая принимает в качестве параметра список,
    # содержащий 1 или 0 элементов, то функция "quick_sort" сразу возвращает этот список,
    # поскольку если список содержит 1 или 0 элементов, то он уже отсортирован по возрастанию.
    # Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
    # ----------
    # Create the base case.
    # The base case in a recursive function is a part of the function code that describes
    # the condition for the termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "quick_sort" takes the list containing 1 or 0 elements
    # as a parameter, then we exit this recursively called copy of the function "quick_sort"
    # and it returns this list to the previous copy of the function "quick_sort"
    # in the call stack, since if a list contains 1 or 0 element, then this list is already sorted in ascending order.
    # If the function "quick_sort" is initially called with the list containing 1 or 0 elements as a parameter,
    # then the function "quick_sort" immediately returns this list,
    # since if a list contains 1 or 0 element, then this list is already sorted in ascending order.
    # The function "print()" prints the specified message to the screen, or other standard output device.
    if len(list_to_sort) < 2:
        return list_to_sort
    # Создаем рекурсивный случай.
    # Рекурсивный случай в рекурсивной функции - это часть кода функции, в которой функция вызывает сама себя
    # в целях выполнения какой-либо задачи.
    # Если список "list_to_sort" содержит 2 или больше элементов, то:
    # ----------
    # Create the recursive case.
    # The recursive case in a recursive function is a part of the function code
    # in which the function calls itself in order to perform a task.
    # If the list "list_to_sort" contains 2 or more elements, then:
    else:
        # 1. Создается переменная "pivot", которая хранит опорный элемент списка "list_to_sort",
        # который равен элементу списка "list_to_sort" под индексом 0.
        # ----------
        # 1. The variable "pivot", that stores the pivot element of the list "list_to_sort",
        # which is equal to the element of the list "list_to_sort" at index 0, is created.
        pivot = list_to_sort[0]
        # 2. Формируется подсписок элементов списка "list_to_sort",
        # которые меньше или равны опорному элементу списка "list_to_sort".
        # Для этого мы перебираем все элементы списка "list_to_sort",
        # кроме первого элемента этого списка, при помощи цикла for,
        # и сохраняем в подсписке "less" только те элементы, которые меньше или равны опорному элементу.
        # ----------
        # 2. The sublist of the elements of the list "list_to_sort",
        # which are less than or equal to the pivot element of the list "list_to_sort", is formed.
        # To do this, we iterate over all the elements of the list "list_to_sort",
        # except for the first element of this list, using a for loop, and store in the sublist "less"
        # only those elements which are less than or equal to the pivot element.
        less = [i for i in list_to_sort[1:] if i <= pivot]
        # 3. Формируется подсписок элементов списка "list_to_sort",
        # которые больше опорного элемента списка "list_to_sort".
        # Для этого мы перебираем все элементы списка "list_to_sort",
        # кроме первого элемента этого списка, при помощи цикла for,
        # и сохраняем в подсписке "greater" только те элементы, которые больше опорного элемента.
        # ----------
        # 3. The sublist of the elements of the list "list_to_sort",
        # which are greater than the pivot element of the list "list_to_sort", is formed.
        # To do this, we iterate over all the elements of the list "list_to_sort",
        # except for the first element of this list, using a for loop,
        # and store in the sublist "greater" only those elements which are greater than the pivot element.
        greater = [i for i in list_to_sort[1:] if i > pivot]
        # 4. Рекурсивно вызываются копии функции "quick_sort" для подсписков "less" и "greater",
        # при этом результаты работ этих рекурсивно вызванных копий функции "quick_sort" конкатенируются
        # с опорным элементом (["less" + "pivot" + "greater"]).
        # Когда рекурсивно вызывается копия функции "quick_sort", которая принимает в качестве параметра список,
        # содержащий 1 или 0 элементов, то срабатывает базовый случай.
        # Копии функции "quick_sort" в стеке вызовов поочередно завершают свою работу и
        # возвращают свои рассчитанные значения предыдущим рекурсивно вызванным копиям функции "quick_sort" до тех пор,
        # пока не завершит работу самая первая вызванная функция "quick_sort".
        # ----------
        # 4. Copies of the function "quick_sort" are recursively called for the sublists "less" and "greater",
        # and the results of these recursively called copies of the function "quick_sort"
        # are concatenated to the pivot element (["less" + "pivot" + "greater"]).
        # When a copy of the function "quick_sort" is recursively called with the list containing 1 or 0 elements
        # as a parameter, then the base case is triggered.
        # The copies of the function "quick_sort" in the call stack terminate one by one and return
        # their calculated values to the previous recursively called copies of the function "quick_sort"
        # until the very first called function "quick_sort" stops its work.
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Пытаемся отсортировать список [2, 0, 6, 9, 7, 7] по возрастанию.
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Try to sort the list [2, 0, 6, 9, 7, 7] in ascending order.
# The function "print()" prints the specified message to the screen, or other standard output device.
print(quick_sort([2, 0, 6, 9, 7, 7]))
