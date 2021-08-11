import os,sys

def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

def coroutine_test():
    '''
    协程(Coroutine)，是数据的消费者。
    >>> coroutine_test()
    ('Searching for', 'coroutine')
    I love coroutine instead!
    I love coroutine!
    '''
    search = grep('coroutine')
    # 这样做正是为了启动一个协程。
    # 就像协程中包含的生成器并不是立刻执行，而是通过next()方法来响应send()方法。
    # 因此，你必须通过next()方法来执行yield表达式。
    next(search)
    #output: Searching for coroutine
    
    search.send("I love you")
    search.send("Don't you love me?")
    search.send("I love coroutine instead!")
    search.send("I love coroutine!")

    # 关闭协程
    search.close()

if __name__ == '__main__':
    from doctest import testmod
    testmod()
