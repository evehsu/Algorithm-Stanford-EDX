from collections import defaultdict


def load_file(f):
    array = []
    with open(f, mode='r') as file:
        for line in file:
            array.append(int(line.strip()))
    return array


def load_adjacent_list(f):
    mygraph = defaultdict(dict)
    with open(f, mode='r') as file:
        for line in file:
            line_s = line.strip().split("\t")
            cur_v = line_s[0]
            for vertex in line_s[1:]:
                mygraph[cur_v][vertex] = 1
    return mygraph