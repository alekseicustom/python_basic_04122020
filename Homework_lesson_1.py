"""Задание 1"""
number1 = 50
number2 = 33
print(number2, number1)

user_name = input('Введите Ваше имя')
user_age = input('Введите Ваш возраст')
print('Здравствуйте,', user_name, 'возраст', user_age)

"""Задание 2"""
user_time = input('Введите время в секундах')
if user_time.isdigit():
    user_time = int(user_time)
else:
    print('Ошибка ввода, введите число')
    exit()
# расчет часов
if user_time >= 3600:
    time_hour = user_time // 3600
    user_time = user_time - time_hour * 3600
else:
    time_hour = 0
# расчет минут
time_minutes = user_time // 60
user_time = user_time - time_minutes * 60
# расчет секунд
time_seconds = user_time % 60

print(time_hour, ':', time_minutes, ':', time_seconds)

"""Задание 3"""
user_number = input('Введите число')
if user_number.isdigit():
    summa = int(user_number) + int(user_number + user_number) + int(user_number + user_number + user_number)
else:
    print('Ошибка ввода, введите число')
    exit()
print(summa)

"""Задание 4"""
user_num = input('Введите целое положительное число:')
if user_num.isdigit():
    user_num = int(user_num)
else:
    print('Ошибка ввода, введите число')
    exit()

mas = []
while user_num > 10:
    mas.append(user_num % 10)
    user_num = user_num // 10
else:
    mas.append(user_num)

max_number = max(mas)
print('Самое большое число', max_number)

"""Задание 5"""
user_proceeds = input('Введите выручку организации:')
user_costs = input('Введите издержки организации:')

if user_proceeds.isdigit() or user_costs.isdigit():
    user_proceeds = int(user_proceeds)
    user_costs = int(user_costs)
else:
    print('Ошибка ввода, введите число')
    exit()

if user_proceeds > user_costs:
    print('Фирма работает с прибылью')
    profitability = (user_proceeds / user_costs) * 100
    print('Рентабельность выручки', "%.2f" % profitability, '%')
else:
    print('Фирма работает с убытком')

user_personal = input('Введите количество сотрудников фирмы:')
if user_personal.isdigit():
    user_personal = int(user_personal)
else:
    print('Ошибка ввода, введите число')
    exit()

profit_personal = (user_proceeds - user_costs) / user_personal
print('Прибыль фирмы на каждого человека', "%.2f" % profit_personal)

"""Задание 6"""
user_a = input('Введите параметр a:')
user_b = input('Введите параметр b:')

if user_a.isdigit() or user_b.isdigit():
    user_a = int(user_a)
    user_b = int(user_b)
else:
    print('Ошибка ввода, введите число')
    exit()

i = 1
while user_a < user_b:
    print(i, '-й день', '-', "%.2f" % user_a)
    user_a = user_a * 1.1
    i = i + 1
else:
    print(i, '-й день', '-', "%.2f" % user_a)
    print('На', i, '-й день спортсмен достиг результата — не менее', user_b, 'км')
