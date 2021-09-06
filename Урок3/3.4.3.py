a = int(input("Введите значение:"))
n = int(input("Введите степень:"))
s=1
for i in range(abs(n)):
    if a == 0:
        s=0
    elif n == 0:
        s=1
    elif n == 1:
        s=a
    elif n < 0:

        s=s*(1 / (a))
    else:
        s =s*a
print(f"{a} в степени {n}= {s}")
