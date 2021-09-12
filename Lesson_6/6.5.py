"""Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Ручка пишет"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Карандаш пишет"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Маркер пишет"


a = Pen('Parker')
print(a.title, a.draw())

b = Pencil('Erich Krause')
print(b.title, b.draw())
c = Handle('touch')
print(c.title, c.draw())
