#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

class Item:
    def name(self):
        pass
    def packing(self):
        pass
    def price(self):
        pass

class Packing:
    def pack(self):
        return ''

class Burger(Item):
    def name(self):
        return 'Burger'
    def packing(self):
        return Wrapper()
    def price(self):
        pass

class VegBurger(Burger):
    def name(self):
        return 'Veg Burger'
    def price(self):
        return 25.0

class ChickenBurger(Burger):
    def name(self):
        return 'Chicken Burger'
    def price(self):
        return 50.0

class ColdDrink(Item):
    def name(self):
        return 'ColdDrink'
    def packing(self):
        return Bottle()

class Pepsi(ColdDrink):
    def name(self):
        return 'Pepsi'
    def price(self):
        return 35.0

class Coke(ColdDrink):
    def name(self):
        return 'Coke'
    def price(self):
        return 30.0

class Wrapper(Packing):
    def pack(self):
        return 'Wrapper'

class Bottle(Packing):
    def pack(self):
        return 'Bottle'

class Meal:
    def __init__(self):
        self._items = []
    @property
    def items(self):
        if self._items == None:
            self._items = []
        return self._items
    def addItem(self, item):
        self.items.append(item)
    def getCost(self):
        cost = 0
        for i in self.items:
            cost += i.price()

        return cost
    
    def showItems(self):
        for i in self.items:
            print('Items: ' + i.name())
            print('Packning: ' + i.packing().pack())
            print('Price: ' + str(i.price()))


class MealBuilder:
    def preVegMeal(self):
        meal = Meal()
        meal.addItem(VegBurger())
        meal.addItem(Coke())
        return meal

    def preNoVegMeal(self):
        meal = Meal()
        meal.addItem(ChickenBurger())
        meal.addItem(Pepsi())
        return meal



if __name__ == '__main__':
    mealbuilder = MealBuilder()
    vegMeal = mealbuilder.preVegMeal()
    print('VegMeal')
    vegMeal.showItems()
    print('Cost: ' + str(vegMeal.getCost()))

    noVegMeal = mealbuilder.preNoVegMeal()
    print('NoVegMeal')
    noVegMeal.showItems()
    print('Cost: ' + str(noVegMeal.getCost()))
