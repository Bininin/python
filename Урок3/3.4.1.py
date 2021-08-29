a = int(input("Введите значение:"))
n = int(input("Введите степень:"))
def my_func(a,n):
    if a == 0:
        s=0
        return s
    elif n == 0:
        s=1
        return s
    elif n == 1:
        return a
    elif n < 0:
        s=(1 / (a*(my_func(a, -n-1))))
        return s
    else:
        s = a*my_func(a, n-1)
        return s


s = my_func(a,n)
print(f"{a} в степени {n}= {s}")
