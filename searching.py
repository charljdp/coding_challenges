'''
Searching algorithms
'''

def linear_search(a: list, value: int):
    for i in range(0, len(a)):
        if a[i] == value:
            return i
    return -1

def binary_search_iter(arr: list, value: int):
    a = 0
    b = len(arr) - 1
    while a <= b:
        m = (a + b)//2
        if value == arr[m]:
            return m
        if value > arr[m]:
            a = m + 1
        elif value < arr[m]:
            b = m - 1
    return -1

def binary_search_rec(
    arr: list, 
    low: int, 
    high: int, 
    value: int
):
    m = (low + high)//2
    if arr[m] == value:
        return m
    if arr[m] < value:
        low = m + 1
    else:
        high = m - 1
    if low > high:
        return -1
    return binary_search_rec(list(arr), low, high, value)

