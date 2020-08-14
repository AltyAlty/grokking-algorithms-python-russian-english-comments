# Обратный отсчет, используя рекурсию.
# ----------
# Countdown using recursion.


# Создаем функцию "countdown", которая принимает один входной параметр:
# число "i", обозначающее число секунд для отсчета.
# ----------
# Create the function "countdown" that accepts one parameter:
# the number "i" representing the number of seconds to count down.
def countdown(i):
    # Создаем базовый случай.
    # Базовый случай в рекурсивной функции - это часть функции, в которой описывается
    # условие прекращения работы функции в целях предотвращения зацикливания.
    # Если секунд для отсчета больше не осталось, то мы выходим из функции. Это наш базовый случай.
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # ----------
    # Create the base case.
    # Base case in a recursive function is a part of a function that describes
    # a condition for termination of the function in order to prevent loops.
    # If there is no seconds to count down, then we exit the function. This is our base case.
    # The keyword "return" is to exit a function and return a value.
    if i < 0:
        return
    # Создаем рекурсивный случай.
    # Рекурсивный случай в рекурсивной функции - это часть функции, в которой функция вызывает сама себя
    # в целях выполнения какой-либо задачи.
    # Выводим число на экран при помощи функции "print()" и вызываем рекурсивно функцию "countdown"
    # с параметром, уменьшенным на 1. Это наш рекурсивный случай.
    # Когда параметр функции "countdown" становится меньше 0, то сработает базовый случай и работа функции завершится.
    # ----------
    # Create the recursive case.
    # Recursive case in a recursive function is a part of a function
    # in which the function calls itself in order to perform some task.
    # Print the number to the screen using the function "print()" and recursively call the function "countdown"
    # with the parameter decreased by 1. This is our recursive case.
    # When the parameter of the function "countdown" is less than 0,
    # then the base case is triggered and the function stops its work.
    else:
        print(i)
        return countdown(i-1)


# Пытаемся вывести на экран отсчет от 6 до 0.
# ----------
# Try to display the countdown from 6 to 0.
countdown(6)
