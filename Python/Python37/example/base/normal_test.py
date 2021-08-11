from collections import deque
import math, time

def coast_time(func):
    def fun(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print('func %s coast time: %.7f s' % (func.__name__, (time.time() - t)))
        
        return result

    return fun

def jump_search(arr, x):
    """
    Pure Python implementation of the jump search algorithm.
    Examples:
    >>> jump_search([0, 1, 2, 3, 4, 5], 3)
    3
    >>> jump_search([-5, -2, -1], -1)
    2
    >>> jump_search([0, 5, 10, 20], 8)
    -1
    >>> jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55)
    10
    """

    n = len(arr)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1

@coast_time
def bogo_sort(collection):
    """Pure implementation of the bogosort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> bogo_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bogo_sort([])
    []
    >>> bogo_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def is_sorted(collection):
        if len(collection) < 2:
            return True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not is_sorted(collection):
        random.shuffle(collection)
    return collection

if __name__ == "__main__":
    from doctest import testmod

    #testmod()

    import random
    
    list_my = [20, 16, 10, 5, 6, 7, 8, 34, 67]
    for i in range(1000):
        val = int(random.random() * 10000)
        #list_my.append(val)
    random.shuffle(list_my)
    print "random.shuffle: ",  list_my

    bogo_sort(list_my)
    print "bogo_sort: ",  list_my

    list_my.append(4)
    bogo_sort(list_my)
    print "bogo_sort: ",  list_my
    #random.shuffle(list_my)
    #print "random.shuffle: ",  list_my
