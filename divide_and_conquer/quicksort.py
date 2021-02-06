import sys
from utils import load_file


class Result:
    def __init__(self):
        self.cnt = 0


def count_comparison(mylist, pivot):

    '''
    :param mylist:input array for count comparison
    :param pivot: choosing pivot method, select from ["first", "final", "median"]
    :return: number of comparison during quicksort
    '''

    result = Result()
    helper(mylist, pivot, result)
    return result.cnt


def helper(mylist, pivot, result):
    if len(mylist) <= 1:
        return
    result.cnt += len(mylist) - 1
    pivot_idx = get_index(mylist, pivot)
    pivot_pos = partition(mylist, pivot_idx)
    helper(mylist[:pivot_pos], pivot, result)
    helper(mylist[pivot_pos + 1:], pivot, result)


def partition(mylist, idx):
    mylist[0], mylist[idx] = mylist[idx], mylist[0]
    i, j = 1, 1
    while j < len(mylist):
        if mylist[j] > mylist[0]:
            j += 1
        else:
            mylist[i], mylist[j] = mylist[j], mylist[i]
            i += 1
            j += 1
    mylist[0], mylist[i - 1] = mylist[i - 1], mylist[0]
    return i - 1


def get_index(mylist, pivot):
    if pivot == "first":
        return 0
    if pivot == "final":
        return len(mylist) - 1
    if pivot == "median":
        middle = len(mylist) // 2 if len(mylist) % 2 > 0 else len(mylist) // 2 - 1
        if mylist[0] <= mylist[middle] < mylist[-1] or mylist[-1] < mylist[middle] <= mylist[0]:
            return middle
        if mylist[middle] < mylist[0] < mylist[-1] or mylist[-1] < mylist[0] < mylist[middle]:
            return 0
    return len(mylist) - 1



def main():
    file_name = sys.argv[1]
    mylist = load_file(file_name)
    mylist1, mylist2, mylist3 = mylist.copy(), mylist.copy(), mylist.copy()
    print(count_comparison(mylist1, 'first'))
    print(count_comparison(mylist2, 'final'))
    print(count_comparison(mylist3, 'median'))

if __name__ =="__main__":
    main()