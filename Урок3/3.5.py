s = 0
b = 0
while b == 0:
    a = (input("Введите значения через пробел (для прекращения опеции нажмите E) :").split())
    for i in range(len(a)):
        try:
            s = s + int(a[i])
        except ValueError:
            if a[i].upper() == "E":
                b = 1
            pass
    print("Сумма элементов: ",s)
