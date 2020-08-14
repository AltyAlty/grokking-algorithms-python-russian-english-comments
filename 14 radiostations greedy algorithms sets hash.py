# Жадный алгоритм, используя множества и хеш-таблицы (словари).
# Здесь нам нужно найти набор радиостанций для покрытия определенного количество штатов, используя жадный алгоритм.
# ----------
# Greedy algorithm using sets and hash tables (dictionaries).
# Here we need to find a set of radio stations to cover a certain number of states using a greedy algorithm.


# Множество - это тип структуры данных, похожий на список, который не может иметь дубликаты.
# Создаем множество "states_needed", которое хранит перечень штатов для покрытия.
# ----------
# Set is a list-like type of data structure that cannot have duplicates.
# Create the set "states_needed" that stores a list of states to cover.
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "са", "az"}


# Создаем словарь "stations", в котором его ключи представляет из себя имена радиостанций,
# а его значения представляют из себя штаты для покрытия этими радио станциями.
# В этом словаре значения являются множествами.
# ----------
# Create the dictionary "stations" in which its keys are the names of radio stations
# and its values are the states for coverage by these radio stations.
# The values are sets in this dictionary.
stations = {"kone": {"id", "nv", "ut"},
            "ktwo": {"wa", "id", "mt"},
            "kthree": {"or", "nv", "са"},
            "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}}


# Создаем множество "final_stations", которое хранит итоговый набор радиостанций для покрытия штатов.
# Изначально этот словарь пустой.
# ----------
# Create the set "final_stations" that stores a final set of radio stations to cover the states.
# Initially this set is empty.
final_stations = set()


# Создаем цикл while, который генерирует итоговый набор радиостанций для покрытия штатов "final_stations".
# Этот цикл while работает, пока множество "states_needed" не является пустым,
# то есть пока у нас имеются непокрытые штаты.
# ----------
# Create the while loop that generates the final set of radio stations to cover the states "final_stations".
# This while loop works as long as the set "states_needed" is not empty, that is,
# as long as we have uncovered states.
while states_needed:
    # Создаем переменную "best_station", которая хранит имя радиостанции,
    # покрывающей больше всего штатов, которые еще не покрыты.
    # Изначально эта переменная хранит "None".
    # ----------
    # Create the variable "best_station" that stores a name of the radio station
    # that covers the most states that are not yet covered.
    # Initially this variable stores "None".
    best_station = None
    # Создаем переменную "states_covered", которая хранит множество штатов,
    # которые еще не покрыты и могут быть покрыты радиостанцией "best_station".
    # Изначально эта переменная хранит пустое множество.
    # ----------
    # Create the variable "states_covered" that stores a set of states that are not yet covered
    # and can be covered by the radio station "best_station".
    # Initially this variable stores an empty set.
    states_covered = set()
    # Создаем цикл for, в котором мы перебираем все ключи ("station") и значения ("states_for_station")
    # в словаре "stations" и находим радиостанцию "best_station".
    # ----------
    # Create the for loop in which we iterate over all the keys ("station") and values ("states_for_station")
    # in the dictionary "stations" and find the radio station "best_station".
    for station, states_for_station in stations.items():
        # Создаем переменную "covered", которая хранит множество штатов,
        # которые еще не покрыты и которые могут быть покрыты текущей радиостанцией "station".
        # Мы находимо это множество путем пересечения следующих множеств:
        # 1. "states_needed" - множество еще не покрытых штатов.
        # 2. "states_for_station" - множество штатов, которые может покрыть текущяя радиостанция "station".
        # ----------
        # Create the variable "covered" that stores a set of states
        # that are not yet covered and can be covered by the current radio station "station".
        # We find this set by intersecting the following sets:
        # 1. "states_needed" - the set of the states that are not yet covered.
        # 2. "states_for_station" - the set of the states that can be covered by the current radio station "station".
        covered = states_needed & states_for_station
        # Если множество "covered" больше, чем множество "states_covered", то
        # ----------
        # If the set "covered" is greater than the set "states_covered", then
        if len(covered) > len(states_covered):
            # текущая радиостанция "station" становится новой лучшей радиостанцией "best_station",
            # ----------
            # the current radio station "station" becomes the new best radio station "best_station",
            best_station = station
            # а также мы обновляем множество "states_covered".
            # ----------
            # and also we update the set "states_covered".
            states_covered = covered
    # После работы каждого цикла for мы уменьшаем перечень штатов, которые необходимо покрыть,
    # вычитая список штатов, которые покрываются текущей лучшей радиостанцией "best_station".
    # Мы это делаем путем вычитания из множества "states_needed" множества "states_covered".
    # ----------
    # After each cycle of the for loop, we reduce the list of the states to be covered
    # by subtracting the list of the states that are covered by the current best radio station "best_station".
    # We do this by subtracting the set "states_covered" from the set "states_needed".
    states_needed -= states_covered
    # А также после работы каждого цикла for мы добавляем текущуюю лучшую радиостанцию "best_station"
    # в итоговый набор радиостанций "final_stations".
    # Для добавления нового элемента в множества мы используем метод "add".
    # ----------
    # And also after each cycle of the for loop, we add the current best radio station "best_station"
    # to the final set of radio stations "final_stations".
    final_stations.add(best_station)


# Выводим на экран итоговый набор радиостанций для покрытия штатов "final_stations".
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Display the final set of the radio stations to cover the states "final_stations".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(final_stations)
