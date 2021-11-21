from abc import ABC,abstractmethod
import random

class MagazineV():
    def __init__(self, name, specialization):
        self.name = name
        self.type = specialization

    def show_info(self):
        print(self.name, self.type)

class Vendor(MagazineV):

    def __init__(self, name, sale):
        self.name = name
        self.sale = sale
        self.tread = None

    def greetings(self):
        print("Здравствуйте. Чем вам помочь?".format())
        self.show_goods()
        self.tread = input("Вы сделали свой выбор?")
        if self.tread in self.sale:
            print(self.tread and self.sale[self.tread])
        else:
            print('Данного продукта сейчас нет в наличии, завтра мы его доставим')

    def show_goods(self):
        print(self.sale)

class Buyer():
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


sale = {"продукт1": 100, "продукт2": 150, "продукт3": 25}
vendor = Vendor("Bob", sale)

vendor.greetings()