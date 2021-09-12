def func():
    name = (input("Введите Имя:"))
    fname = (input("Введите Фамилию:"))
    born = (input("Введите год рождения:"))
    city = (input("Введите город:"))
    email = (input("Введите e-mail:"))
    phone = (input("Введите номер телефона:"))
    data = name + " " + fname + " " + born + " " + city + " " + email + " " + phone
    return data


data = func()
print("Данные: ", data)
