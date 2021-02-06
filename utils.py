def load_file(f):
    array = []
    with open(f, mode='r') as file:
        for line in file:
            array.append(int(line.strip()))
    return array