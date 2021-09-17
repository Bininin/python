def my_func(a,b,c):
    s = a + b + c - min(a, b, c)
    return s


s = my_func(a = int(input("Введите первый элемент:")),
    b = int(input("Введите второй элемент:")),
    c = int(input("Введите третий элемент:")))
print("Сумма двух максимальных элементов: ", s)
