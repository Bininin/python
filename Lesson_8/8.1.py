"""Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках
класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""
a = "12-09-2021"


class Data:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @staticmethod
    def get_data(obj):
        if 1 <= int(obj.d) <= 31 and 1 <= int(obj.m) <= 12 and 0 <= int(obj.y) <= 2021:
            return f"{int(obj.d):02d} {int(obj.m):02d} {int(obj.y):02d}"
        else:
            return f"Не верные даты"

    @classmethod
    def set_data(cls, data):
        d, m, y = data
        return cls(d, m, y)


data_list = list(a.split("-"))
print(data_list)
dat1 = Data.set_data(data_list)

print(Data.get_data(dat1))
