a = int(input("Введите натуральное число: "))
b = [7, 5, 3, 3, 2]
print("Рейтинг до: ")
for i in range(len(b)):
    if a > int(b[i]):
        print(b[i])
        b.insert(i, a)
        break
    else:
        b.append(a)
        break
print("Рейтинг после: ")
print(b)
