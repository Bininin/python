a = int(input("Введите натуральное число: "))
b = [7, 5, 3, 3, 2]
b.append(0)
print("Рейтинг до: ", b)
for i in range(len(b)):
    print(b[i], i)
    if a > b[i]:
        b.insert((i), a)
        break
print("Рейтинг после: ")
print(b)
