from sys import argv

a, b, c, d = argv
print("Имя скрипта: ", str(a))
print("Количество часов, ч: ", b)
print("Ставка в час,", chr(8381), ": ", c)
print("Премия,", chr(8381), ": ", d)
s = int(b) * int(c) + int(d)
print("Итого: ", s, chr(8381))
