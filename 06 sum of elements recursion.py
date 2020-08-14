# Сумма элементов, используя рекурсию.
# ----------
# Sum of elements using recursion.


# Создаем функцию "sum_of_elem", которая принимает один входной параметр:
# список "list_of_elem", содержащий элементы для суммирования.
# ----------
# Create the function "sum_of_elem" that accepts one parameter:
# the list "list_of_elem" containing the elements to add.
def sum_of_elem(list_of_elem):
    # Создаем базовый случай.
    # Базовый случай в рекурсивной функции - это часть функции, в которой описывается
    # условие прекращения работы функции в целях предотвращения зацикливания.
    # Если одна из вызванных рекурсивно копий функции "sum_of_elem" принимает в качестве параметра список,
    # содержащий 0 элементов, то мы выходим из этой копии функции "sum_of_elem" и возвращаем число "0"
    # предыдущей копии функции "sum_of_elem" в стеке вызовов, поскольку сумма 0 элементов всегда равна 0.
    # Если изначально вызывается функция "sum_of_elem", которая принимает в качестве параметра список,
    # содержащий 0 элементов, то функция "sum_of_elem" сразу возвращает число "0", поскольку сумма 0 элементов
    # всегда равна 0.
    # Функция "len()" возвращает количество элементов в списке.
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # ----------
    # Create the base case.
    # Base case in a recursive function is a part of a function that describes
    # a condition for termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "sum_of_elem" takes a list containing 0 elements
    # as a parameter, then we exit this recursively called copy of the function "sum_of_elem"
    # and it returns the number "0" to the previous copy of the function "sum_of_elem" in a call stack,
    # since the sum of 0 elements is always 0.
    # If the function "sum_of_elem" is initially called with a list containing 0 elements as a parameter,
    # then the function "sum_of_elem" immediately returns the number "0", since the sum of 0 elements is always 0.
    # The function "len()" returns the number of elements in a list.
    # The keyword "return" is to exit a function and return a value.
    if len(list_of_elem) == 0:
        return 0
    # Создаем рекурсивный случай.
    # Рекурсивный случай в рекурсивной функции - это часть функции, в которой функция вызывает сама себя
    # в целях выполнения какой-либо задачи.
    # Рекурсивно вызываем копию функции "sum_of_elem" со списком "list_of_elem" в качестве входного параметра,
    # за исключением первого элемента в этом списке, при этом результат работы этой рекурсивно вызванной копии
    # функции "sum_of_elem" суммируется с первым элементом входного параметра текущей копии функции "list_of_elem".
    # Когда рекурсивно вызывается копия функции "sum_of_elem", которая принимает в качестве параметра список,
    # содержащий 0 элементов, то срабатывает базовый случай.
    # Копии функции "sum_of_elem" в стеке вызовов поочередно завершают свою работу
    # и возвращают свои рассчитанные значения предыдущим рекурсивно вызванным копиям функции "sum_of_elem" до тех пор,
    # пока не завершит работу самая первая вызванная функция "sum_of_elem".
    # ----------
    # Create the recursive case.
    # Recursive case in a recursive function is a part of a function
    # in which the function calls itself in order to perform some task.
    # Recursively call a copy of the function "sum_of_elem" with the list "list_of_elem" as a parameter,
    # except for the first element of this list, while the result of
    # this recursively called copy of the function "sum_of_elem" is summed up with the first element of the parameter
    # of the current copy of the function "sum_of_elem".
    # When a copy of the function "sum_of_elem" is recursively called with a list containing 0 elements
    # as a parameter, then the base case is triggered.
    # The copies of the function "sum_of_elem" in the call stack terminate one by one and return their calculated values
    # to the previous recursively called copies of the function "sum_of_elem"
    # until the very first called function "sum_of_elem" stops its work.
    else:
        return list_of_elem[0] + sum_of_elem(list_of_elem[1:])


# Попытаемся найти сумму 13, 7, 37, 7, 5.
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Try to find the sum of 13, 7, 37, 7, 5.
# The function "print()" prints the specified message to the screen, or other standard output device.
print(sum_of_elem([13, 7, 37, 7, 5]))
