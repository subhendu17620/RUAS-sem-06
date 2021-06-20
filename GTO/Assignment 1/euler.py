
from pyvis.network import Network
from collections import defaultdict
from copy import copy


class Graph:
    # Constructor
    def __init__(self, edges, N):

        # A list of lists to represent an adjacency list
        self.adjList = defaultdict(lambda: [])

        # for visualizing the graph
        self.net = Network()
        self.net.add_nodes(list(range(N)))
        self.net.add_edges(edges)

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

    def visualize(self, x):
        allEd = self.net.get_edges()
        for j in allEd:
            j.pop('color', None)
            j.pop('width', None)
        ctr = ord('a')-1
        for edge in x:
            for j in allEd:
                if (j['from'] == edge[0] and j['to'] == edge[1]) or (j['from'] == edge[1] and j['to'] == edge[0]):
                    ctr += 1
                    j['color'] = 'rgba(0, 196, 154,0.5)'
                    j['width'] = 5
                    j['label'] = chr(ctr)


# is_connected - Checks if a graph in the form of a dictionary is
# connected or not, using Breadth-First Search Algorithm (BFS)
def is_connected(G):
    start_node = list(G)[0]
    color = {v: 'white' for v in G}
    color[start_node] = 'gray'
    S = [start_node]
    while len(S) != 0:
        u = S.pop()
        for v in G[u]:
            if color[v] == 'white':
                color[v] = 'gray'
                S.append(v)
            color[u] = 'black'
    return list(color.values()).count('black') == len(G)

# odd_degree_nodes - returns a list of all G odd degrees nodes


def odd_degree_nodes(G):
    odd_degree_nodes = []
    for u in G:
        if len(G[u]) % 2 != 0:
            odd_degree_nodes.append(u)
    return odd_degree_nodes


# from_dict - return a list of tuples links from a graph G in a
# dictionary format
def from_dict(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u, v))
    return links


# fleury(G) - return eulerian trail from graph G or a
# string 'Not Eulerian Graph' if it's not possible to trail a path
def fleury(G):

    # checks if G has eulerian cycle or trail
    odn = odd_degree_nodes(G)
    if len(odn) > 2 or len(odn) == 1:
        return 'Not Eulerian Graph'
    else:
        g = copy(G)
        trail = []
        if len(odn) == 2:
            u = odn[0]
        else:
            u = list(g)[0]
        while len(from_dict(g)) > 0:
            current_vertex = u
            for u in g[current_vertex]:
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                bridge = not is_connected(g)
                if bridge:
                    g[current_vertex].append(u)
                    g[u].append(current_vertex)
                else:
                    break
            if bridge:
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                g.pop(current_vertex)
            trail.append((current_vertex, u))
    return trail


# # testing seven bridges of konigsberg
# print('Konigsberg Graph')
# G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
# print(fleury(G))


# testing eulerian cycle
G = {0: [1, 2, 3, 4],
     1: [2, 3, 4, 0],
     2: [3, 4, 0, 1],
     3: [4, 0, 1, 2],
     4: [0, 1, 2, 3]}

res = fleury(G)
print("Euler Cycle: ", res)

# visualising graph
g = Graph([(0, 1), (0, 2), (0, 3), (0, 4),
           (1, 2), (1, 3), (1, 4),
           (2, 3), (2, 4),
           (3, 4)], 5)

g.visualize(res)
g.net.show("a.html")
