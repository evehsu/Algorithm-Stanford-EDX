import sys
from utils import load_file

def count_inversion(array):
    if len(array) == 1:
        return 0, array

    mid = len(array) // 2
    left_cnt, left_array = count_inversion(array[:mid])
    right_cnt, right_array = count_inversion(array[mid:])
    split_cnt, merge_array = count_split_merge(left_array, right_array)
    return left_cnt + right_cnt + split_cnt, merge_array


def count_split_merge(left_arr, right_arr):
    output_arr = [0] * (len(left_arr) + len(right_arr))
    i, j = 0, 0
    split_cnt = 0
    for k in range(len(output_arr)):
        if i == len(left_arr):
            output_arr[k] = right_arr[j]
            j += 1
        elif j == len(right_arr):
            output_arr[k] = left_arr[i]
            i += 1
        elif left_arr[i] <= right_arr[j]:
            output_arr[k] = left_arr[i]
            i += 1
        else:
            split_cnt += len(left_arr) - i
            output_arr[k] = right_arr[j]
            j += 1
    return split_cnt, output_arr


def main():
    file_name = sys.argv[1]
    mylist = load_file(file_name)
    print(len(mylist))
    print(mylist[:10])
    print(count_inversion(mylist)[0])
    print(count_inversion(mylist)[1][:10])



if __name__== "__main__":
    main()