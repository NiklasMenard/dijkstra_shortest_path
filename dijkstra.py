import sys
from collections import defaultdict
import time


def print_path(width_list, node_list, goal_node):

    if node_list.get(goal_node):

        path = [str(goal_node)]
        smallest_width = []
        while goal_node is not None:
            previous_node = node_list[goal_node]
            smallest_width.append(width_list[goal_node])
            if previous_node is not None:
                path.append(str(previous_node))
            goal_node = node_list[goal_node]

        path.reverse()
        del smallest_width[-1]
        print("->".join(path))
        print(max(smallest_width))

    else:
        print("Path to node does not exits")


def creategraph(file):

    graph = defaultdict(list)
    data = open(file, 'r')
    temp_graph = defaultdict(list)
    goal_node = 0

    node_amount = data.readline().split(' ')
    for i in range(1, int(node_amount[0])):
        graph[i] = []

    for line in data:
        if len(line.strip().split()) is 1:
            goal_node = line.strip().split()[0]
        else:
            node, nextnode, weight = map(int, line.strip().split())
            graph[node].append((nextnode, weight))

    for keynode, neighbour_nodes in graph.items():
        for node in neighbour_nodes:
            nodetoadd, weight = node
            temp_graph[nodetoadd].append((keynode, weight))

    for key, neighbour_nodes in temp_graph.items():
        for node in neighbour_nodes:
            graph[key].append(node)

    data.close()

    return int(goal_node), graph


class Dijkstra:

    def __init__(self, graph):

        self.graph = graph

    def printgraph(self):

        for node, connected_nodes in self.graph.items():
            print(node, connected_nodes)

    def getneighbours(self, nodenumber):

        neighbours = []
        for i in range(len(self.graph[nodenumber])):
            neighbours.append(self.graph.get(nodenumber)[i])

        return neighbours

    def dijkstra(self):

        distances = dict.fromkeys(self.graph.keys())
        distances.update((key, sys.maxsize) for key in distances)
        distances[1] = 0
        previous_node = dict.fromkeys(self.graph.keys())
        unvisited = dict.fromkeys(self.graph.keys())

        visited = set()
        while unvisited:

            current_node = None
            min_distance = sys.maxsize

            for node in unvisited:
                if distances[node] < min_distance and node not in visited:
                    min_distance = distances[node]
                    current_node = node

            neighbours = self.getneighbours(current_node)
            for neighbour, weight in neighbours:
                # swap out relaxation condition below to get the path with smallest width
                # alt_route = max(distances[current_node], weight)
                alt_route = distances[current_node] + weight
                if alt_route < distances[neighbour]:
                    distances[neighbour] = alt_route
                    previous_node[neighbour] = current_node

            del unvisited[current_node]
            visited.add(current_node)

        return distances, previous_node


def main():

    goal_node, graph = creategraph(input("Type in file name > ") + ".txt")
    d = Dijkstra(graph)
    widths, previous_nodes = d.dijkstra()
    print_path(widths, previous_nodes, goal_node)


start_time = time.clock()
main()
print(time.clock() - start_time, "seconds")
