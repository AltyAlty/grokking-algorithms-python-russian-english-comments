# Вывод приветствия.
# Здесь мы создаем две функции, которые вызываются из третьей функции.
# Здесь мы можем рассмотреть работу стека вызовов.
# ----------
# Printing greetings.
# Here we create two functions, that are called by the third function.
# Here we can see how the call stack works.


# Создаем функцию "how_are_you", которая выводит на экран текст "How are you, username ?" при помощи функции "print()".
# Эта функция принимает один входной параметр: имя "username" того, кого приветствуют.
# ----------
# Create the function "how_are_you" that prints the message "How are you, username ?" to the screen
# using the function "print()".
# This function accepts one parameter: the name "username" of the person being greeted.
def how_are_you(username):
    print("How are you,", username, "?")


# Создаем функцию "bye", которая выводит на экран текст "Ok, bye!" при помощи функции "print()".
# Эта функция не принимает никаких входных параметров.
# ----------
# Create the function "bye" that prints the message "Ok, bye!" to the screen using the function "print()".
# This function doesn't have any parameters.
def bye():
    print("Ok, bye!")


# Создаем функцию "greet", которая выводит на экран текст "Hello, username !" при помощи функции "print()",
# а также вызывает функции "how_are_you" и "bye".
# Эта функция принимает один входной параметр: имя "username" того, кого приветствуют.
# ----------
# Create the function "greet" that prints the message "Hello, username !" to the screen using the function "print()"
# and calls the functions "how_are_you" and "bye".
# This function accepts one parameter: the name "username" of the person being greeted.
def greet(username):
    # Стек вызовов содержит функцию "greet".
    # Функция "greet" выполняет свою работу: выводит на экран
    # сообщение "Hello, username !" при помощи функции "print()".
    # ----------
    # The call stack contains the function "greet".
    # The function "greet" does its work: it prints
    # the message "Hello, username !" to the screen using the function "print()".
    print("Hello,", username, "!")
    # Функция "greet" вызывает функцию "how_are_you".
    # В стеке вызовов работа функции "greet" приостанавливается.
    # В стек вызовов наверх добавляется функция "how_are_you".
    # Функция "how_are_you" выполняет свою работу: выводит на экран сообщение "How are you, username ?"
    # ----------
    # The function "greet" calls the function "how_are_you".
    # The function "greet" is suspended in the call stack.
    # The function "how_are_you" is added to the call stack.
    # The function "how_are_you" does its work: it prints the message "How are you, username ?" to the screen.
    how_are_you(username)
    # Функция "how_are_you" завершает свою работу, передает управление функции "greet" и убирается из стека вызовов.
    # Функция "greet" возобновляет свою работу и выводит на экран
    # текст "Ok, bye in 3 .. 2 .. 1" при помощи функции "print()".
    # ----------
    # The function "how_are_you" exits, transfers control to the function "greet" and is removed from the call stack.
    # The function "greet" resumes and prints
    # the message "Ok, bye in 3 .. 2 .. 1" to the screen using the function "print()".
    print("Ok, bye in 3 .. 2 .. 1")
    # Функция "greet" вызывает функцию "bye".
    # В стеке вызовов работа функции "greet" приостанавливается.
    # В стек вызовов наверх добавляется функция "bye".
    # Функция "bye" выполняет свою работу: выводит на экран сообщение "Ok, bye!"
    # ----------
    # The function "greet" calls the function "bye".
    # The function "greet" is suspended in the call stack.
    # The function "bye" is added to the call stack.
    # The function "bye" does its work: it prints the message "Ok, bye!" to the screen.
    bye()
    # Функция "bye" завершает свою работу, передает управление функции "greet" и убирается из стека вызовов.
    # Функция "greet" возобновляет свою работу.
    # Функция "greet" завершает свою работу убирается из стека вызовов.
    # ----------
    # The function "bye" exits, transfers control to the function "greet" and is removed from the call stack.
    # The function "greet" resumes.
    # The function "greet" exits and is removed from the call stack.


# Пытаемся поприветствовать пользователя John Shepard.
# ----------
# Try to greet user John Shepard.
greet("John Shepard")
