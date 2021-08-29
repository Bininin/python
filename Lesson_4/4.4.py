import random

b = []
"""
Создание рандомного списка из количества элементов введенных пользователем
"""


def list_r():
    a = 10
    try:
        a = int(input("Введите количество элементов списка:"))
    except ValueError:
        print("Вы введи не число (по умолчанию 10 элементов)")
    except UnboundLocalError:
        print("введите число2")
    except TypeError:
        print("введите число3")
        a = 0
    for i in range(a):
        b.append(int(random.randint(1, 10)))


list_r()
print("Первоначальный список:\n", b)
c = []

"""
функция выдающая список из уникальных элементов
"""


def sr():
    for i in range(len(b)):
        if b.count(b[i]) == 1:
            c.append(b[i])
    return c


print(f"Полученный список:\n {sr()} \nколичество уникальных элементов {len(c)} из {len(b)}")
