import os
import sys

import types
import inspect
from inspect import isfunction

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

@logit()
def logit_test():
    pass

@logit('out1.log')
def logit_test1():
    pass

def func_test():
    logit_test()

    logit_test1()

from distutils.msvccompiler import MSVCCompiler

class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, logfile='email_out.log', email='admin@myproject.com', *args, **kwargs):
        #logit.__init__(self, logfile)
        super(logit, self).__init__(*args, **kwargs)
        self.logfile = logfile

        self.email = email

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        print('send to email')
        pass

@email_logit()
def addition_func():
    print('addition_func')

if __name__ == "__main__":
    func_test()

    addition_func()