import os,sys
import io

# 上下文管理器允许你在有需要的时候，精确地分配和释放资源。

class File(object):
    '''
    一个上下文管理器的类，最起码要定义__enter__和__exit__方法。
    通过定义__enter__和__exit__方法，我们可以在with语句里使用它。
    '''
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        if not type is None:
            print("%s Exception has been handled, message: %s" % (self.__class__, value))
        self.file_obj.close()
        return True

from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()

def contextmanager_test():
    '''
    >>> contextmanager_test()
    '''
    
    with open('some_file.txt', 'w+') as opened_file:
        opened_file.seek(0, io.SEEK_END)
        opened_file.write('Hola!\n')
    
    '''
    1.with语句先暂存了File类的__exit__方法
    2.然后它调用File类的__enter__方法
    3.__enter__方法打开文件并返回给with语句
    4.打开的文件句柄被传递给opened_file参数
    5.我们使用.write()来写文件
    6.with语句调用之前暂存的__exit__方法
    7.__exit__方法关闭了文件
    '''
    with File('some_file.txt', 'w+') as opened_file:
        opened_file.seek(0, io.SEEK_END)
        opened_file.write('Hola!\n')

if __name__ == '__main__':
    from doctest import testmod
    testmod()

    print(dir())
    with File('some_file.txt', 'w+') as opened_file:
        opened_file.undefined_function()

    with open_file('some_file.txt') as f:
        f.write('hola!')