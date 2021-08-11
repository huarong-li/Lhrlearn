import time
import timeit
import sys

from functools import lru_cache

@lru_cache()
def func():
    print('func start')
    time.sleep(1)
    print('func end')


if __name__ == '__main__':
    print(timeit.timeit(stmt=func, number=1))

    if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
        print(sys.version_info)

    from coast_time import test
    test()

    