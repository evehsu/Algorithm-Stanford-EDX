import sys
from utils import load_adjacent_list
import random


def kargerMinCut(graph):
    '''
    :param graph: graph represent by adjacent list: {node :[connected nodes]}
    :param edges: all edges of graph in a RandomizedSet
    :return: remaining edges after partition the graph into 2
    '''
    while len(graph) > 2:
        # pick an edge randomly
        r_vertex = random.choice(list(graph.keys()))
        r_vertex_connections = list(graph[r_vertex].keys())
        r_connection = random.choice(r_vertex_connections)
        r_edge = (r_vertex, r_connection)
        clean_up(graph,r_edge)
    remain_vertices = list(graph.keys())
    v1, v2 = remain_vertices[0], remain_vertices[1]
    return graph[v1][v2]


def clean_up(graph,e):

    '''

    :param graph:
    :param edges:
    :param e: edge that will be collapsed , tuple (node1, node2)
    :return: nothing, but graph are after collapse the two vertices of e
    '''

    v1, v2 = e[0], e[1]

    # we'll always keep the vertex with smaller index, which is v1
    for connect_vertex in graph[v2]:
        # handle invalid vertex
        graph[connect_vertex].pop(v2, None)
        if connect_vertex != v1:
            if connect_vertex in graph[v1]:
                graph[v1][connect_vertex] += graph[v2][connect_vertex]
                graph[connect_vertex][v1] += graph[v2][connect_vertex]
            else:
                graph[v1][connect_vertex] = graph[v2][connect_vertex]
                graph[connect_vertex][v1] = graph[v2][connect_vertex]
    graph.pop(v2, None)
    return

def mincut(g):
    while len(g) > 2:
        c1 = random.choice(range(len(g)))
        v_del = g.pop(c1)
        c2 = random.choice(range(1, len(v_del)))
        v1, v2 = v_del[0], v_del[c2]
        while v2 in v_del:
            v_del.remove(v2)
        for i in range(len(g)):
            if g[i][0] == v2:
                g[i] += v_del
                while v1 in g[i]:
                    g[i].remove(v1)
            for j in range(len(g[i])):
                g[i][j] = v2 if g[i][j] == v1 else g[i][j]
    return len(g[0])-1


def main():

    file_name = sys.argv[1]
    global_min = float("inf")

    for i in range(1000):
        mygraph= load_adjacent_list(file_name)
        # mygraph = load_tmp(file_name)
        global_min = min(global_min, kargerMinCut(mygraph))
        print(mygraph)
        print(global_min)


if __name__ == "__main__":
    main()
