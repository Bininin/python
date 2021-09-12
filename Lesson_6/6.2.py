"""Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● опредна*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода."""


class Road:
    def __init__(self, length, width, height, massa=2400):
        self._length = length
        self._width = width
        self._height = height
        self._massa = massa

    def mass(self):
        return  self._length * self._width * (self._height / 1000) * (self._massa / 1000)


r = Road(int(input("Длина дороги (м)")), int(input("Ширина дороги (м)")), int(input("Толщина полотна (мм)")))
print(f"----------------------------\nРассход асфальта {r.mass()} т")
