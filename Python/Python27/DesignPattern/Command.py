#!/usr/bin/python
# -*- coding:utf-8 -*-

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

