"""
4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going...')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn(self, direction):
        print(f'{self.name} is turned {direction}')

    def show_speed(self):
        print(f'{self.name} is moving with {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} is moving too fast.')
        else:
            print(f'{self.name} is moving with {self.speed} km/h')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} is moving too fast.')
        else:
            print(f'{self.name} is moving with {self.speed} km/h')


class PoliceCar(Car):
    pass


tc = TownCar(100, 'blue', 'Granta')
sc = SportCar(200, 'green', 'F1')
wk = WorkCar(50, 'grey', 'tractor')
pc = PoliceCar(150, 'red', 'ford', True)
print(tc.is_police)
tc.stop()
sc.show_speed()
wk.show_speed()
print(pc.is_police)
