from functools import singledispatch
from linked_list import LinkedList


def selection_sort(a: list):
    pass


@singledispatch
def insertion_sort(a: list):
    pass


@insertion_sort.register
def insertion_sort(a: LinkedList):
    pass



def shell_sort(a: list):
    pass


def quick_sort(a: list):
    pass


def merge_sort(a: LinkedList):
    pass


def heap_sort(a: list):
    pass
