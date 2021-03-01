import sys
from utils import load_dijkstra_graph
from collections import defaultdict


def dijkstra(graph, s, t):
    '''

    :param graph: adjacent list of directed graph
    :param s: source node
    :param t: target node
    :return: shortest path returned by dijkstra algorithm
    '''

    visited = {s : 0}
    while t not in visited:
        next_edge_tail, next_edge_head, next_dist = find_next(graph,visited)
        visited[next_edge_head] = next_dist
    return visited[t]


def find_next(graph, visited):
    '''
    iterate every edge that from visited to unvisited, and find the minimum as next node in shortest path
    :param graph:
    :param visited:
    :return:
    '''
    cur_node_visited = list(visited.keys())
    next_head, next_tail = None, None
    global_min = float("inf")
    for n in cur_node_visited:
        cur_heads = list(graph[n].keys())
        for h in cur_heads:
            if h in visited:
                continue
            if visited[n] + graph[n][h] < global_min:
                next_head, next_tail = h, n
                global_min = visited[n] + graph[n][h]

    return next_tail, next_head, global_min

def main():
    file_name = sys.argv[1]
    g = load_dijkstra_graph(file_name)
    res = []
    s = 1
    for t in [7,37,59,82,99,115,133,165,188,197]:
        sp = dijkstra(g, s, t)
        res.append(sp)
    print(res)


if __name__ == "__main__":
    main()