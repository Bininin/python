a=int(input("Введите номер месяца: "))
# print("Первоначальный список:\n", a)
d={1: "Январь",2: "Февраль",12: "Декабрь", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь" }
l=["Зима","Зима","Весна","Весна","Весна","Лето","Лето","Лето","Осень","Осень","Осень","Зима"]
print("Месяц: ",d.get(a),"\nВремя года: ", l[a-1])