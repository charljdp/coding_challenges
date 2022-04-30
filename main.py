from searching import binary_search_iter, binary_search_rec
from sorting import bubble_sort

def test_binary_search_rec():
    print(binary_search_rec([55,444,514,523,578,668,859], 0, 6, 55))
    print(binary_search_rec([55,444,514,523,578,668,859], 0, 6, 444))
    print(binary_search_rec([55,444,514,523,578,668,859], 0, 6, 514))
    print(binary_search_rec([55,444,514,523,578,668,859], 0, 6, 523))
    print(binary_search_rec([55,444,514,523,578,668,859], 0, 6, 578))
    print(binary_search_rec([55,444,514,523,578,668,859], 0, 6, 668))
    print(binary_search_rec([55,444,514,523,578,668,859], 0, 6, 859))
    print(binary_search_rec([55,444,514,523,578,668,859], 0, 6, 75))


def test_binary_search_iter():
    # print(binary_search([1,22,333], 1))
    # print(binary_search([1,22,333], 22))
    # print(binary_search([1,22,333], 333))
    # print(binary_search([1,22,333], 33))
    print('----------------------------------------------')
    print(binary_search_iter([55,444,514,523,578,668,859], 55))
    print(binary_search_iter([55,444,514,523,578,668,859], 444))
    print(binary_search_iter([55,444,514,523,578,668,859], 514))
    print(binary_search_iter([55,444,514,523,578,668,859], 523))
    print(binary_search_iter([55,444,514,523,578,668,859], 578))
    print(binary_search_iter([55,444,514,523,578,668,859], 668))
    print(binary_search_iter([55,444,514,523,578,668,859], 859))
    print(binary_search_iter([55,444,514,523,578,668,859], 75))
    print('----------------------------------------------')

def test_bubble_sort():
    x = [3,1,66,33,2,0,1,4,6,222,7]
    bubble_sort(x)
    print(x)

if __name__ == '__main__':
    test_bubble_sort()