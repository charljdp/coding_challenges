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
    m = a + (b - a)//2
    while a < b:
        if value > arr[m]:
            a = m + 1
        if value < arr[m]:
            b = m - 1
        m = a + (b - a)//2
        if value == arr[m]:
            return m
    return -1


if __name__ == '__main__':
    print(binary_search([1,22,333], 1))
    print(binary_search([1,22,333], 22))
    print(binary_search([1,22,333], 333))
    print(binary_search([1,22,333], 33))
    print('----------------------------------------------')
    print(binary_search([55,444,514,523,578,668,859], 55))
    print(binary_search([55,444,514,523,578,668,859], 444))
    print(binary_search([55,444,514,523,578,668,859], 514))
    print(binary_search([55,444,514,523,578,668,859], 523))
    print(binary_search([55,444,514,523,578,668,859], 578))
    print(binary_search([55,444,514,523,578,668,859], 668))
    print(binary_search([55,444,514,523,578,668,859], 859))
    print(binary_search([55,444,514,523,578,668,859], 75))
    print('----------------------------------------------')
