How the algorithm works:

The algorithm works by reading nodes from a text file and creating an undirected graph from this data. The assumption is that the starting node is always 1. 
Dijkstra algorithm is implement after the graph has been formed. If the textfile has been typed out correctly, it will print out the path to the goal node
and the sum of the path edges weight


How to test algorithm:

Type in name of textfile without .txt. You can also use test file from the graph_testdata and graph_large_testdata folders. Textfile must be in same folder as the dijkstra.py file

If you want to create you own text file it must be typed out following these rules:

First row is two values separated by a space: number of nodes and number of edges.

After the first row all the nodes and their weights are typed in three values separated by an space: starting node, connected node and weight between the nodes.

On the last line is the goal node. Below you can see and example:

7 9
1 2 73
1 3 70
1 4 85
2 4 78
2 5 50
3 6 60
4 7 75
5 7 80
6 7 80
7






                                                                            
