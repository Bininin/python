a = int(input("Введите значение:"))
n = int(input("Введите степень:"))


def my_func(a, n):
    s = a ** (n)
    return s


s = my_func(a, n)
print(f"{a} в степени {n}= {s}")
