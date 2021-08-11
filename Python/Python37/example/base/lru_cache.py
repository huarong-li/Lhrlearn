from functools import wraps

def lru_cache(fun):
    '''
    缓存函数的返回值，提升执行速度。
    '''
    cache = {}
    @wraps(fun)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            value = fun(*args)
            cache[args] = value
            return value
    return wrapper

'''
递归函数写法，存在大量的重复计算。
在Python 3.2版本以前我们只有写一个自定义的实现。
Python 3.2以后版本，有个lru_cache的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。
@lru_cache(maxsize=32),
那个maxsize参数是告诉lru_cache，最多缓存最近多少个返回值。
使用fib.cache_clear()轻松地对返回值清空缓存。
'''
@lru_cache
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_test():
    '''
    >>> fibonacci_test()
    39088169
    '''
    print(fibonacci(38))

if __name__ == '__main__':
    from doctest import testmod
    testmod()