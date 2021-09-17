a = int(input("введите число: "))
y = 1
b = []
for i in range(a):
    b.append(y)
    y += 1


def generator():
    for el in b:

        yield el


g = generator()

fakt = 1
for el in g:
    fakt = fakt * int(el)
    print(f"факториал числа {el} = {fakt}")
