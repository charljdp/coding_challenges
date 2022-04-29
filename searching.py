'''
Searching algorithms
'''

def linear_search(a: list, value: int):
    for i in range(0, len(a)):
        if a[i] == value:
            return i
    return -1

def binary_search(arr: list, value: int):
    a = 0
    b = len(arr) - 1
    while a < b:
        m = (b - a)//2
        if value == arr[m]:
            return m
        if value > arr[m]:
            a = m
        if value < arr[m]:
            b = m
    return -1

if __name__ == '__main__':
    print(binary_search([1,22,333], 22))