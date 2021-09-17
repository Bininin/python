"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата."""

class Komp:
    def __init__(self, p1, p2):
        self.p1 = int(p1)
        self.p2 = int(p2)

    def plus(self, other):
        return Komp(self.p1 + other.p1, self.p2 + other.p2)

    def mul(self, other):
        return Komp((self.p1) * (other.p1) - (self.p2) * (other.p2), (self.p1) * (other.p2) + (self.p2) * (other.p1))

    def __str__(self):
        if (self.p2) >= 0:
            return f"{(self.p1)}+{(self.p2)}i"
        else:
            return f"{(self.p1)}{(self.p2)}i"


c1 = Komp(1, 2)
c2 = Komp(3, 4)

print(Komp.plus(c1, c2))
print(Komp.mul(c1, c2))
