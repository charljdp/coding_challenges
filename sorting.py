from functools import singledispatch
from linked_list import LinkedList


def swap(lst, idx1, idx2):
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp


def bubble_sort(lst: list[int]):
    '''
    Efficiency: O(n^2)
    '''
    n = len(lst)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if (lst[i] < lst[i + 1]):
                swap(lst, i, i + 1)
                swapped = True
        n -= 1


def selection_sort(lst: list):
    '''
    Efficiency: O(n^2)
    '''
    n = len(lst)
    for i in range(n):
        minimum = lst[i]
        for j in range(i + 1, n):
            if lst[j] < minimum:
                minimum = lst[j]
                min_j = j
        swap(lst, i, min_j)


# @singledispatch
def insertion_sort(lst: list):
    '''
    Efficiency: O(n^2). Typically faster than bubble sort.
    '''
    n = len(lst)
    for i in range(n):
        index = i
        ins_value = lst[index]
        while (index > 0 and ins_value < lst[index - 1]):
            lst[index] = lst[index - 1]
            index -= 1
        lst[index] = ins_value


# @insertion_sort.register
# def insertion_sort(a: LinkedList):
#     pass



def shell_sort(a: list):
    pass


def quick_sort(a: list):
    pass


def merge_sort(a: LinkedList):
    pass


def heap_sort(a: list):
    pass
