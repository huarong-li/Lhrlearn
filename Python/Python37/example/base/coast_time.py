import sys
import time
import timeit

def coast_time(func):
    def fun(*args, **kwargs):
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
            t = time.perf_counter()
        else:
            t = time.time()
        result = func(*args, **kwargs)
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
            t1 = time.perf_counter()
        else:
            t1 = time.time()
        print('func %s coast time: %.7f s' % (func.__name__, t1 - t))
        return result

    return fun

@coast_time
def test():
    print('func start')
    time.sleep(1)
    print('func end')

if __name__ == '__main__':
    print(timeit.timeit(stmt=test, number=1))
