# Подсчет элементов используя рекурсию.
# ----------
# Counting elements using recursion.


# Создаем функцию "count", которая принимает один входной параметр:
# список "list_of_elem", содержащий элементы для подсчета.
# ----------
# Create the function "count" that accepts one parameter:
# the list "list_of_elem" containing the elements to count.
def count(list_of_elem):
    # Создаем базовый случай.
    # Базовый случай в рекурсивной функции - это часть кода функции, в которой описывается
    # условие прекращения работы функции в целях предотвращения зацикливания.
    # Если одна из вызванных рекурсивно копий функции "count" принимает в качестве параметра список,
    # содержащий 0 элементов, то мы выходим из этой копии функции "count" и возвращаем число "0"
    # предыдущей копии функции "count" в стеке вызовов, поскольку количество элементов в списке с 0 элементов
    # всегда равно 0.
    # Если изначально вызывается функция "count", которая принимает в качестве параметра список,
    # содержащий 0 элементов, то функция "count" сразу возвращает число "0", поскольку количество элементов
    # в списке с 0 элементов всегда равно 0.
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # ----------
    # Create the base case.
    # The base case in a recursive function is a part of the function code that describes
    # the condition for the termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "count" takes the list containing 0 elements
    # as a parameter, then we exit this recursively called copy of the function "count"
    # and it returns the number "0" to the previous copy of the function "count" in the call stack,
    # since the number of elements in the list with 0 elements is always 0.
    # If the function "count" is initially called with the list containing 0 elements as a parameter,
    # then the function "count" immediately returns the number "0", since the number of elements
    # in the list with 0 elements is always 0.
    # The keyword "return" is to exit a function and return a value.
    if len(list_of_elem) == 0:
        return 0
    # Создаем рекурсивный случай.
    # Рекурсивный случай в рекурсивной функции - это часть кода функции, в которой функция вызывает сама себя
    # в целях выполнения какой-либо задачи.
    # Рекурсивно вызываем копию функции "count" со списком "list_of_elem" в качестве входного параметра,
    # за исключением первого элемента в этом списке, при этом результат работы этой рекурсивно вызванной копии
    # функции "count" увеличивается на 1.
    # Когда рекурсивно вызывается копия функции "count", которая принимает в качестве параметра список,
    # содержащий 0 элементов, то срабатывает базовый случай.
    # Копии функции "count" в стеке вызовов поочередно завершают свою работу
    # и возвращают свои рассчитанные значения предыдущим рекурсивно вызванным копиям функции "count" до тех пор,
    # пока не завершит работу самая первая вызванная функция "count".
    # ----------
    # Create the recursive case.
    # The recursive case in a recursive function is a part of the function code
    # in which the function calls itself in order to perform a task.
    # Recursively call a copy of the function "count" with the list "list_of_elem" as a parameter,
    # except for the first element of this list, while the result of
    # this recursively called copy of the function "count" is is increased by 1.
    # When a copy of the function "count" is recursively called with the list containing 0 elements
    # as a parameter, then the base case is triggered.
    # The copies of the function "count" in the call stack terminate one by one and return their calculated values
    # to the previous recursively called copies of the function "count"
    # until the very first called function "count" stops its work.
    else:
        return 1 + count(list_of_elem[1:])


# Создаем список чисел "my_list".
# ----------
# Create the list of numbers "my_list".
my_list = [2, 0, 6, 9, 7, 7]


# Попытаемся подсчитать элементы в списке "my_list".
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Try to count elements in the list "my_list".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(count(my_list))
