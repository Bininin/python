from functools import reduce

a = [a for a in range(100, 1001) if a % 2 == 0]
print(a)


def pr(b1, b2):
    return b1 * b2


print("Произведение всех четный числе в диапазоне от 100 до 1000 включительно:\n", reduce(pr, a))
