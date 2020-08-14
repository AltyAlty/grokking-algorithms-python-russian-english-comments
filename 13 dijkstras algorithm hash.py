# Алгоритм Дейкстры, используя хеш-таблицы (словари).
# Здесь нам нужно найти все кратчайшие пути от начального узла до всех остальных узлов
# в направленном ациклическом взвешенном графе.
# ----------
# Dijkstra's algorithm using hash tables (dictionaries).
# Here we need to find all the shortest paths from a start node to all other nodes
# in a directed acyclic weighted graph.


# Создаем словарь "graph", который представляет из себя направленный ациклический взвешенный граф.
# Этот словарь особенный тем, что каждое его значение является словарем.
# Эти значения представляют из себя наборы соседних узлов каждого узла этого графа и их стоимостей.
# ----------
# Create the dictionary "graph" which is a directed acyclic weighted graph.
# This dictionary is special in that each of its value is a dictionary.
# These values are the sets of neighboring nodes of each node of this graph and their costs.
graph = {"start": {"a": 6,
                   "b": 2},
         "a": {"fin": 1},
         "b": {"a": 3,
               "fin": 5},
         "fin": {}}


# Создаем переменную "infinity", которая хранит "бесконечность".
# Мы используем эту переменную, когда неизвестен путь до какого-либо узла.
# ----------
# Create the variable "infinity" that stores "infinity".
# We use this variable when a path to a node is unknown.
infinity = float("inf")


# Создаем словарь "costs", который представляет из себя таблицу стоимостей
# путей от узла "start" до других узлов графа "graph".
# Указываем те стоимости, которые известны в начале работы алгоритма.
# В комментариях ниже указаны изменения значений после работы каждого цикла while,
# который находится внизу этой программы.
# ----------
# Create the dictionary "costs" which is a table of costs of the paths from the node "start"
# to the other nodes of the graph "graph".
# We specify those costs that are known at the beginning of the algorithm.
# The comments below show the changes of the values after each cycle of the while loop,
# which is located at the bottom of this program.
costs = {"a": 6,            # 5 - 5 - 5
         "b": 2,            # 2 - 2 - 2
         "fin": infinity}   # 7 - 6 - 6


# Создаем словарь "parents", который представляет из себя таблицу родителей каждого узла в графе "graph".
# Указываем тех родителей, которые известны в начале работы алгоритма.
# В комментариях ниже указаны изменения значений после работы каждого цикла while,
# который находится внизу этой программы.
# ----------
# Create the dictionary "parents" which is a table of the parents of each node in the graph "graph".
# We specify those parents that are known at the beginning of the algorithm.
# The comments below show the changes of the values after each cycle of the while loop,
# which is located at the bottom of this program.
parents = {"a": "start",    # "b"     - "b"     - "b"
           "b": "start",    # "start" - "start" - "start"
           "fin": None}     # "b"     - "a"     - "a"


# Создаем список "processed", в который мы добавляем уже обработанные узлы,
# чтобы избежать повторной обработки таких узлов.
# Изначально этот список пустой.
# ----------
# Create the list "processed" to which we add already processed nodes
# to avoid reprocessing such nodes.
# Initially this list is empty.
processed = []


# Создаем функцию "find_lowest_cost_node", которая принимает один входной параметр:
# словарь "table_of_costs", который представляет из себя таблицу стоимостей
# путей от начального узла до других узлов направленного ациклическего взвешенного графа.
# Эта функция возвращает имя узла с наименьшей стоимостью.
# ----------
# Create the function "find_lowest_cost_node" that accepts one parameter:
# the dictionary "table_of_costs" which is a table of costs of paths from a start node
# to other nodes of a directed acyclic weighted graph.
# This function returns a name of the lowest cost node.
def find_lowest_cost_node(table_of_costs):
    # Создаем переменную "lowest_cost", которая хранит стоимость узла, который имеет наименьшую стоимость.
    # Изначально эта переменная хранит значение "бесконечность".
    # ----------
    # Create the variable "lowest_cost" that stores the cost of the lowest cost node.
    # Initially this variable stores the value "infinity".
    lowest_cost = float("inf")
    # Создаем переменную "lowest_cost_node", которая хранит имя узла, который имеет наименьшую стоимость.
    # Изначально эта переменная хранит значение "None".
    # ----------
    # Create the variable "lowest_cost_node" that stores the name of the lowest cost node.
    # Initially this variable stores "None".
    lowest_cost_node = None
    # Создаем цикл for, в котором перебираем все ключи (узлы графа) словаря "table_of_costs".
    # ----------
    # Create the for loop in which we iterate over all the keys (graph nodes) of the dictionary "table_of_costs".
    for key_node in table_of_costs:
        # Создаем переменную "value_cost", которая хранит значение (стоимость узла графа),
        # соответствующее текущему ключу.
        # ----------
        # Create the variable "value_cost" that stores the value (cost of a graph node)
        # corresponding to the current key.
        value_cost = table_of_costs[key_node]
        # Если стоимость текущего узла меньше стоимости узла, который имеет наименьшую стоимость,
        # и если мы еще не обрабатывали этот текущий узел, то
        # ----------
        # If the cost of the current node is less than the cost of the lowest cost node,
        # and if we have not yet processed this current node, then
        if value_cost < lowest_cost and key_node not in processed:
            # считаем, что стоимость текущего узла является наименьшей,
            # ----------
            # we consider that the cost of the current node is the lowest,
            lowest_cost = value_cost
            # а также считаем, что этот узел является новым узлом, который имеет наименьшую стоимость.
            # ----------
            # and we also consider that this node is the new lowest cost node.
            lowest_cost_node = key_node
    # В итоге работы этого цикла for функция "find_lowest_cost_node" возвращает имя узла с наименьшей стоимостью.
    # Ключевое слово "return" выходит из функции и возвращает какое-либо значение.
    # ----------
    # As a result of this for loop, the function "find_lowest_cost_node" returns the name of the lowest cost node.
    # The keyword "return" is to exit a function and return a value.
    return lowest_cost_node


# Находим имя узла с наименьшей стоимостью в словаре "costs" (изначально это узел "b").
# В комментариях ниже указаны изменения значений этой переменной после работы каждого цикла while,
# который находится внизу этой программы.
# ----------
# Find the name of the lowest cost node in the dictionary "costs" (initially it is the node "b").
# The comments below show the changes of the value of this variable after each cycle of the while loop,
# which is located at the bottom of this program.
node = find_lowest_cost_node(costs)  # "a" - "fin" - None


# Высчитываем все кратчайшие пути от узла "start" до узлов "a", "b" и "fin"
# путем обновления словарей "costs" и "parents".
# Создаем цикл while, который работает пока переменная "node" не является пустой,
# то есть пока у нас есть узлы с наименьшей стоимостью для обработки.
# ----------
# Calculate all the shortest paths from the node "start" to the nodes "a", "b", "fin"
# by updating the dictionaries "costs" and "parents".
# Create the while loop that works as long as the variable "node" is not empty, that is,
# as long as we have the lowest cost nodes to process.
while node is not None:
    # Создаем переменную "cost", которая хранит стоимость текущего узла с наименьшей стоимостью "node".
    # ----------
    # Create the variable "cost" that stores the cost of the current lowest cost node "node".
    cost = costs[node]
    # Создаем переменную "neighbors", которая хранит словарь, представляющий из себя
    # список соседних узлов текущего узла с наименьшей стоимостью "node" и их стоимости.
    # ----------
    # Create the variable "neighbors", the stores a dictionary which is a list of the neighboring nodes
    # of the current lowest cost node "node" and their costs.
    neighbors = graph[node]
    # Создаем цикл for, в котором перебираем
    # ключи (имена всех соседних узлов текущего узла с наименьшей стоимостью "node") в словаре "neighbors".
    # ----------
    # Create the for loop in which we iterate over the keys (the names of all neighboring nodes
    # of the current lowest cost node "node") in the dictionary "neighbors".
    for neighbor_name in neighbors.keys():
        # Высчитываем новую стоимость пути от узла "start"
        # до текущего соседнего узла текущего узла с наименьшей стоимостью "node".
        # ----------
        # Calculate the new cost of the path from the node "start" to the current neighboring node
        # of the lowest cost node "node".
        new_cost = cost + neighbors[neighbor_name]
        # Если текущая стоимость пути от узла "start"
        # до текущего соседнего узла текущего узла с наименьшей стоимостью "node"
        # больше, чем новая стоимость этого пути, то
        # ----------
        # If the current cost of the path from the node "start" to the current neighboring node
        # of the lowest cost node "node" is greater than the new cost of this path, then
        if costs[neighbor_name] > new_cost:
            # обновляем текущую стоимость этого пути в словаре "costs",
            # ----------
            # we update the current cost of this path in the dictionary "costs",
            costs[neighbor_name] = new_cost
            # а также обновляем родителя текущего соседнего узла текущего узла с наименьшей стоимостью "node"
            # в словаре "parents".
            # ----------
            # and also we update the parent of the current neighboring node
            # of the current lowest cost node "node" in the dictionary "parents".
            parents[neighbor_name] = node
    # Если мы перебрали все соседние узлы текущего узла с наименьшей стоимостью "node",
    # тогда мы добавляем этот узел в список "processed",
    # ----------
    # If we have iterated over all the neighboring nodes of the current lowest cost node "node",
    # then we add this node to the list "processed",
    processed.append(node)
    # находим следующий узел, который имеет наименьшую стоимость,
    # и работа этого цикла while продолжается с начала, используя этот новый узел.
    # ----------
    # find the next lowest cost node
    # and this while loop continues from the beginning using this new node.
    node = find_lowest_cost_node(costs)


# Выводим на экран обновленные словари "costs" и "parents".
# Функция "print()" выводит некую указанную информацию на экран или на какое-либо другое устройство вывода.
# ----------
# Display the updated dictionaries "costs" and "parents".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(costs)
print(parents)
