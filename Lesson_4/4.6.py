from sys import argv
from itertools import count
from itertools import cycle


def count_(a, b):
    for i in count(a, 1):
        if i > b:
            break
        else:
            print(i)


count_(int(input("Введитие начальное число: ")), int(input("Введитие конечное число: ")))


def cycle_(c1, c2):
    y = 0
    c3 = cycle(c1)
    while y < c2:
        print(next(c3))
        y += 1


cycle_(c1=(input("Введитие элементы списка: ").split()), c2=int(input("Введитие количество итераций: ")))
