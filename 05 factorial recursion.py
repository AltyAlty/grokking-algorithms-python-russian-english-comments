# Факториал используя рекурсию.
# ----------
# Factorial using recursion.


# Создаем функцию "fact", которая вычисляет факториал.
# Эта функция принимает один входной параметр: число "x", факториал которого необходимо найти.
# ----------
# Create the function "fact" that calculates the factorial.
# This function accepts one parameter: the number "x", the factorial of which is to be found.
def fact(x):
    # Создаем базовый случай.
    # Базовый случай в рекурсивной функции - это часть кода функции, в которой описывается
    # условие прекращения работы функции в целях предотвращения зацикливания.
    # Если одна из вызванных рекурсивно копий функции "fact" вычисляет факториал числа 1,
    # то мы выходим из этой копии функции и возвращаем число "1" предыдущей копии функции "fact" в стеке вызовов.
    # Если изначально вызывается функция "fact" со входным параметром равным числу 1,
    # то функция "fact" сразу возвращает число 1, поскольку факториал числа 1 равен 1.
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # ----------
    # Create the base case.
    # The base case in a recursive function is a part of the function code that describes
    # the condition for the termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "fact" calculates the factorial of the number 1,
    # then we exit this recursively called copy of the function "fact" and it returns the number "1" to
    # the previous copy of the function "fact" in the call stack.
    # If the function "fact" is initially called with a parameter of 1,
    # then the function "fact" immediately returns the number 1, since the factorial of the number 1 is 1.
    # The keyword "return" is to exit a function and return a value.
    if x == 1:
        return 1
    # Создаем рекурсивный случай.
    # Рекурсивный случай в рекурсивной функции - это часть кода функции, в которой функция вызывает сама себя
    # в целях выполнения какой-либо задачи.
    # Рекурсивно вызываем копию функции "fact" с входным параметром уменьшенным на 1, результат которой множится
    # на значение входного параметра текущей копии функции "fact".
    # Когда рекурсивно вызывается копия функции "fact" с входным параметром равным 1, то срабатывает базовый случай.
    # Копии функции "fact" в стеке вызовов поочередно завершают свою работу и возвращают свои рассчитанные значения
    # предыдущим рекурсивно вызванным копиям функции "fact" до тех пор, пока не завершит работу самая первая вызванная
    # функция "fact".
    # ----------
    # Create the recursive case.
    # The recursive case in a recursive function is a part of the function code
    # in which the function calls itself in order to perform a task.
    # Recursively call a copy of the function "fact" with the parameter decreased by 1,
    # the result of which is multiplied by the value of the parameter of the current copy of the function "fact".
    # When a copy of the function "fact" is recursively called with a parameter of 1, then the base case is triggered.
    # The copies of the function "fact" in the call stack terminate one by one and return their calculated values
    # to the previous recursively called copies of the function "fact"
    # until the very first called function "fact" exits.
    else:
        return x * fact(x-1)


# Пытаемся найти факториал от числа 4.
# ----------
# Try to find the factorial of 4.
print(fact(4))
