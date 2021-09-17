import random

a = int(input("введите количество элементов списка:"))
b = []

"""
Создание рандомного списка из количества элементов введенных пользователем
"""


def list_r():
    for i in range(a):
        b.append(int(random.randint(1, 300)))


list_r()
print("первоначальный список\n", b)
c = []

"""
функция выдающая список из больших элементов по сравнению с следующих за ними элементами
"""


def sr():
    for i in range(len(b) - 1):
        if b[i] > b[i + 1]:
            c.append(b[i])
    return c


print("Полученный список\n", sr())
sr()
