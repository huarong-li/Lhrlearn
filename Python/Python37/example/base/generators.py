import os

# 这会在计算很大的输入参数时，用尽所有的资源。
def fibon_array(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# 使用yield，动态计算，不至于在n过大时占用大量内存
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def generators_test():
    '''
    生成器(Generators),是数据生成者。
    使用内置函数next来获取yield生成的值，它允许我们获取一个序列的下一个元素。
    在yield掉所有的值后，next()触发了一个StopIteration的异常。
    基本上这个异常告诉我们，所有的值都已经被yield完了。
    你也许会奇怪，为什么我们在使用for循环时没有这个异常呢？
    答案很简单。for循环会自动捕捉到这个异常并停止调用next()。
    >>> generators_test()
    1
    1
    2
    3
    5
    8
    13
    end
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    144
    233
    377
    610
    987
    1597
    2584
    4181
    6765
    '''
    n1 = fibon(7)
    print(next(n1))
    print(next(n1))
    print(next(n1))
    print(next(n1))
    print(next(n1))
    print(next(n1))
    print(next(n1))
    print('end')

    for i in fibon(20):
        print(i)
    
    '''
    它是一个可迭代对象，而不是一个迭代器。这意味着它支持迭代，但我们不能直接对其进行迭代操作。
    那我们怎样才能对它实施迭代呢？是时候学习下另一个内置函数，iter。
    它将根据一个可迭代对象返回一个迭代器对象。
    '''
    my_string = "Yasoob"
    my_iter = iter(my_string)
    next(my_iter)

if __name__ == '__main__':
    from doctest import testmod
    testmod()

    print(fibon_array(1000))