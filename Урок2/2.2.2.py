a = input("Введите через пробел элементы списка: ").split()
print("Первоначальный список:\n", a)
b = []
if (len(a) % 2) == 0:
    for i in range(len(a)):
        if i % 2 == 0:
            b.append(a[i + 1])
        elif i % 2 != 0:
            b.append(a[i - 1])
        else:
            b.append(a[i])
else:
    for i in range(len(a)):
        if i % 2 == 0 and (i in range(len(a) - 1)):
            b.append(a[i + 1])
        elif i % 2 != 0:
            b.append(a[i - 1])
        else:
            b.append(a[-1])
print("Измененный список:\n", b)
