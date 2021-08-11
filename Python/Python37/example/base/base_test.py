
import os
import sys

import types
import inspect
from inspect import isfunction

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

def fun(*args,**kwargs):
    """ 函数参数测试， *args 和 **kwargs
    """
    print('args: %s' % (str(args)))
    print('kwargs: %s' % str(kwargs))
    if "key" in kwargs and kwargs["key"] is False:
        print('key is false')

def debugoutput():
    print("debugoutput")

def dosomething(func, *var,**kwargs):
    """ 函数对象类型测试
    """
    if "key" in kwargs and kwargs["key"] is False:
        print(var)
    
    # 使用hasattr判读是否有__call__属性来判断
    fun_type = hasattr(func, '__call__')

    # 使用callable来判断
    fun_type1 = callable(func)

    # 使用isfunction来判断
    fun_type2 = inspect.isfunction(func)

    fun_id = id(func)
    if fun_type:
        func()

    return 0

def fun_test():
    fun(1,2,3)
    fun(1,2,key=False,val=3)

    dosomething(3)
    dosomething(debugoutput)
    
def string_test():
    # （+）操作符拼接
    s = 'Hello'+' '+'World'+'!'
    print(s)

    # 通过str.join()方法拼接
    strlist=['Hello',' ','World','!']
    print(''.join(strlist))

    # 通过str.format()方法拼接
    s='{} {}!'.format('Hello','World')
    print(s)

    # 通过(%)操作符拼接
    s = '%s %s!' % ('Hello', 'World')
    print(s)

    # 通过()多行拼接
    s = (
        'Hello'
        ' '
        'World'
        '!'
    )
    print(s)

def map_test():
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, items))
    print(squared)

    def multiply(x):
        return (x*x)
    def add(x):
        return (x+x)

    funcs = [multiply, add]
    for i in range(5):
        value = map(lambda x: x(i), funcs)
        print(list(value))
    # 译者注：上面print时，加了list转换，是为了python2/3的兼容性
    #        在python2中map直接返回列表，但在python3中返回迭代器
    #        因此为了兼容python3, 需要list转换一下

    # filter使用
    number_list = range(-5, 5)
    less_than_zero = filter(lambda x: x < 0, number_list)
    print(list(less_than_zero)) 

    # reduce使用
    product = reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
    print(product)

if __name__ == "__main__":
    #fun_test()

    string_test()

    map_test()

    # 三元运算符
    is_fat = True
    print("fat" if is_fat else "not fat")
