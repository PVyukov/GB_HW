"""
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import abstractmethod, ABC


class Interface(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Interface):

    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Interface):

    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def consumption(self):
        return 2 * self.h + 0.3


class Clothes(Interface):

    def __init__(self):
        self.items = []

    def add_item(self, type_item, name, var):
        if type_item == 'C':
            self.items.append(Coat(name, var))
        elif type_item == 'S':
            self.items.append(Suit(name, var))
    @property
    def consumption(self):
        consume_total = 0
        for i in self.items:
            consume_total += i.consumption()
        return consume_total


coat = Coat('coat1', 10)
suit = Suit('suit1', 10)
print(f'consumption of {coat.name} is {coat.consumption()}')
print(f'consumption of {suit.name} is {suit.consumption()}')
clothes = Clothes()
clothes.add_item('C', 'coat1', 10)
clothes.add_item('S', 'suit1', 10)
print(f'Total consumption is {clothes.consumption}')


