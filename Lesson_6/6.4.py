"""Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат."""

import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина едет ---"

    def stop(self):
        return "Машина становилась ---"

    def turn(self, direction=["Налево","Направо"]):
        return "Машина повернула " + direction[random.randint(0,1)] + " --- "


class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)
        if speed > 60:
            print("\033[31mПревышение скорости\033[38m")


class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)


class WorkCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)

        if speed > 40:
            print(f"\033[31mПревышение скорости\033[38m ")


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


color = ["красный", "белый", "синий"]
car = ["Toyota", "audi", "lada", "kia", "skoda"]
typecar=[TownCar,SportCar,WorkCar,PoliceCar]
a = typecar[random.randint(0, 3)](car[random.randint(0, 4)], random.randint(10, 100), color[random.randint(0, 2)])
print(a.name, a.color, a.speed, a.is_police,a)
dir=[a.go(), a.turn(), a.stop()]
print(dir[random.randint(0, 2)])

