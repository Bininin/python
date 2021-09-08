a=input("Введите через пробел элементы списка: ").split()
print("Первоначальный список:\n", a)
b=[]
if len(a)%2==0:
    for i in range(len(a)):
        if i%2==0:
            b.append(a[i+1])
        elif i%2!=0:
            b.append(a[i-1])
elif  len(a)%2!=0:
    for i in range(len(a)):
        if i%2==0 and i<(len(a)-1):
            b.append(a[i+1])
        elif i%2!=0:
            b.append(a[i-1])
    b.append(a[i])
print(b)