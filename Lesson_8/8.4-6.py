"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники."""


class Sklad:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            # unit = input(f'Введите наименование ')
            # unit_p = int(input(f'Введите цену за ед '))
            # unit_q = int(input(f'Введите количество '))
            # unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            # self.my_unit.update(unique)
            # self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(Sklad):
    def to_print(self):
        pr = {}
        pr.update(pr)
        return f'Принтеров на складе {self.numb}'


class Scanner(Sklad):
    def to_scan(self):
        pr = {}
        pr.update(pr)

        return f'Сканеров на складе {self.numb}'


class Copier(Sklad):
    def to_copier(self):
        return f'Ксероксов на складе {self.numb}'


print(f'Для выхода - Q, продолжение - Enter')

while True:
    p = input(f'Введите тип устройства поступивщего на склад\n1-Принтер\n2-Сканер\n3-Ксерокс\nдля выходы нажмите q\n:')
    if p == "1":
        mod = input(f'Введите модель принтера: ')
        price = int(input(f'Введите цену за ед: '))
        kol = int(input(f'Введите количество: '))
        poz = {'Модель устройства': mod, 'Цена за ед': price, 'Количество': kol}
        unit_1 = Printer(mod, price, kol, poz)
        # self.my_unit.update(unique)
        # self.my_store.append(self.my_unit)
        print(f'Текущий список -\n {unit_1}')
        # pr={}
        # pr.update(unit_1)

    elif p == "2":

        mod = input(f'Введите модель сканера: ')
        price = int(input(f'Введите цену за ед: '))
        kol = int(input(f'Введите количество: '))
        poz = {'Модель устройства': mod, 'Цена за ед': price, 'Количество': kol}
        unit_2 = Printer(mod, price, kol, poz)
        # self.my_unit.update(unique)
        # self.my_store.append(self.my_unit)
        print(f'Текущий список -\n {unit_2}')

    elif p == "3":
        mod = input(f'Введите модель Ксерокса: ')
        price = int(input(f'Введите цену за ед: '))
        kol = int(input(f'Введите количество: '))
        poz = {'Модель устройства': mod, 'Цена за ед': price, 'Количество': kol}
        unit_3 = Printer(mod, price, kol, poz)
        # self.my_unit.update(unique)
        # self.my_store.append(self.my_unit)
        print(f'Текущий список -\n {unit_3}')
    elif p == "q":
        break

    # unit_1 = Printer('hp', 2000, 5, 10)
# self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

# unit_1 = Printer('hp', 2000, 5, 10)
# unit_2 = Scanner('Canon', 1200, 5, 10)
# unit_3 = Copier('Xerox', 1500, 1, 15)
# print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
# print(unit_3.to_copier())
