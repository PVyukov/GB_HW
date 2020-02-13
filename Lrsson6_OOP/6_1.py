"""
1)	Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
 Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
 Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
 на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
 зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
 Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
 и завершать скрипт
"""
from itertools import cycle
import time


class TrafficLight:
    def __init__(self):
        self.__color = cycle(['red', 'yellow', 'green'])

    def running(self):
        for cur_color in self.__color:
            # while stop != "true":
            delay = 7 if cur_color == 'red' else 2 if cur_color == 'yellow' else 1
            print(cur_color)
            time.sleep(delay)


T1 = TrafficLight()
T1.running()
