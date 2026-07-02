import copy
import sys


def bubble_sort(input_list):
    arr = copy.deepcopy(input_list)
    for n in range(len(arr) - 1, 0, -1):

        swapped = False

        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break
    return arr


def selection_sort(input_list):
    arr = copy.deepcopy(input_list)
    size = len(arr)
    for i in range(size-1):
        min_index = i

        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            (arr[i], arr[min_index]) = (arr[min_index], arr[i])
    return arr


def insertion_sort(input_list):
    arr = copy.deepcopy(input_list)
    size = len(arr)

    for i in range(1, size):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def merge_sort(input_list):
    arr = copy_a_rec(input_list)
    return merge_sort_alg(arr)


def copy_a_rec(input_list):
    sys.setrecursionlimit(100000)
    return copy.deepcopy(input_list)


def merge_sort_alg(arr):
    if len(arr) > 1:

        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]

        L = merge_sort_alg(L)
        R = merge_sort_alg(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def quick_sort(input_list):
    arr = copy_a_rec(input_list)
    return quick_sort_alg(arr)


def quick_sort_alg(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort_alg(left) + [pivot] + quick_sort_alg(right)
