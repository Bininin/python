print([a for a in range(20, 240) if a % 20 == 0 or a % 21 == 0])


# ИЛИ

print({a for a in range(20, 240) if a % 20 == 0 or a % 21 == 0})