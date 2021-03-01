import sys
from utils import load_directed_graph
from collections import defaultdict
sys.setrecursionlimit(2**20)




class FinishTime:
    def __init__(self):
        self.val = 1

def kosaraju(g,n):
    t = FinishTime()
    #reverse graph
    rg = reverse(g)
    # calculate finish time
    finish = get_finish(rg, n, t)
    # rebuild graph by finish time
    fg = rebuild(g, finish)
    # use dict to save leader
    leaders = get_leader(fg, n, {})
    scc = convert(leaders)
    return scc


def reverse(g):
    rg = defaultdict(list)
    for v in g:
        for _v in g[v]:
            rg[_v].append(v)
    return rg


def rebuild(g, finish_arr):
    fg = defaultdict(list)
    for v in g:
        for _v in g[v]:
            fg[finish_arr[v - 1]].append(finish_arr[_v - 1])
    return fg


def get_finish(g, n, ft):
    visited = set()
    res = [0] * n
    for i in range(1, n + 1):
        if i not in visited:
            helper_ft(g, i, visited, res, ft)
    return res


def helper_ft(g, i, visited, res, ft):
    visited.add(i)
    for node in g[i]:
        if node not in visited:
            helper_ft(g, node, visited, res, ft)
    res[i - 1] = ft.val
    ft.val += 1
    return


def get_leader(g, n, res):
    visited = set()
    for i in range(n, 0, -1):
        if i not in visited:
            cur = i
            helper_ld(g, i, visited, res, cur)
    return res


def helper_ld(g, i, visited, res, leader):
    visited.add(i)
    res[i] = leader
    for node in g[i]:
        if node not in visited:
            helper_ld(g, node, visited, res, leader)
    return


def convert(leaders):
    '''

    :param leaders: {node: node_leader}
    :return: {leader_node: [leaded node]}
    '''
    res = defaultdict(list)
    for k, v in leaders.items():
        res[v].append(k)
    return res


def main():

    file_name = sys.argv[1]
    n = sys.argv[2]
    mygraph = load_directed_graph(file_name)
    res_scc = kosaraju(mygraph, int(n))
    size_scc = [len(x) for x in list(res_scc.values())]
    size_scc.sort(reverse=True)
    print(size_scc[:5])
    #[434821, 968, 459, 313, 211]



if __name__ == "__main__":
    main()