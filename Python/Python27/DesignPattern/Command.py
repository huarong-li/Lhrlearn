#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
命令模式
命令模式（Command Pattern）是一种数据驱动的设计模式，它属于行为型模式。请求以命令的形式包裹在对象中，并传给调用对象。调用对象寻找可以处理该命令的合适的对象，并把该命令传给相应的对象，该对象执行命令。
'''

'''
介绍
意图：将一个请求封装成一个对象，从而使您可以用不同的请求对客户进行参数化。

主要解决：在软件系统中，行为请求者与行为实现者通常是一种紧耦合的关系，但某些场合，比如需要对行为进行记录、撤销或重做、事务等处理时，这种无法抵御变化的紧耦合的设计就不太合适。

何时使用：在某些场合，比如要对行为进行"记录、撤销/重做、事务"等处理，这种无法抵御变化的紧耦合是不合适的。在这种情况下，如何将"行为请求者"与"行为实现者"解耦？将一组行为抽象为对象，可以实现二者之间的松耦合。

如何解决：通过调用者调用接受者执行命令，顺序：调用者→命令→接受者。

关键代码：定义三个角色：1、received 真正的命令执行对象 2、Command 3、invoker 使用命令对象的入口

应用实例：struts 1 中的 action 核心控制器 ActionServlet 只有一个，相当于 Invoker，而模型层的类会随着不同的应用有不同的模型类，相当于具体的 Command。

优点： 1、降低了系统耦合度。 2、新的命令可以很容易添加到系统中去。

缺点：使用命令模式可能会导致某些系统有过多的具体命令类。

使用场景：认为是命令的地方都可以使用命令模式，比如： 1、GUI 中每一个按钮都是一条命令。 2、模拟 CMD。

注意事项：系统需要支持命令的撤销(Undo)操作和恢复(Redo)操作，也可以考虑使用命令模式，见命令模式的扩展。
'''

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Order:
    __metaclass__ = ABCMeta
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class BuyOrder(Order):
    def __init__(self, stock):
        super(BuyOrder, self).__init__()
        self._stock = stock

    def execute(self):
        self._stock.buy()

class SellOrder(Order):
    def __init__(self, stock):
        super(SellOrder, self).__init__()
        self._stock = stock

    def execute(self):
        self._stock.sell()

class Stock:
    def __init__(self):
        self._name = 'ABC'
        self._quantity = 10
    
    # def __init__(self, name, quantity):
    #     self._name = name
    #     self._quantity = quantity

    def buy(self):
        print("Stock [ Name: "+self._name+",  Quantity: " + str(self._quantity) +" ] bought")
    def sell(self):
        print("Stock [ Name: "+self._name+",  Quantity: " + str(self._quantity) +" ] sell")

class Broker:
    def __init__(self):
        self._orders = []

    def takeOrder(self, order):
        self._orders.append(order)
    
    def placeOrders(self):
        for item in self._orders:
            item.execute()
        del self._orders[:]


if __name__ == '__main__':
    stock = Stock()

    broker = Broker()

    broker.takeOrder(BuyOrder(stock))
    broker.takeOrder(SellOrder(stock))

    broker.placeOrders()

