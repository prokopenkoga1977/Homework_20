# Задание 1
# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня недели. Например, если 1, то на экране надпись понедельник,
# 2 — вторник и т.д.
number_day = int(input("Enter the number of the day of the week (1-7): "))
if number_day == 1: 
    print ("Monday")
elif number_day == 2: 
    print ("Tuesday")
elif number_day == 3: 
    print ("Wednesday")
elif number_day == 4: 
    print ("Thursday")
elif number_day == 5: 
    print ("Friday")
elif number_day == 6: 
    print ("Saturday")
elif number_day == 7: 
    print ("Sunday")
else: 
     print ("Error")

# Задание 2
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

number_month = int(input("Enter the number of the month (1-12): "))
if number_month == 1: 
    print ("January")
elif number_month == 2: 
    print ("February")
elif number_month == 3: 
    print ("March")
elif number_month == 4: 
    print ("April")
elif number_month == 5: 
    print ("May")
elif number_month == 6: 
    print ("June")
elif number_month == 7: 
    print ("July")
elif number_month == 8:
    print("August")
elif number_month == 9:
    print("September")
elif number_month == 10:
    print("October")
elif number_month == 11:
    print("November")
elif number_month == 12:
    print("December")
else: 
     print ("Error")

# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»

number=int(input("Enter number: "))
if number > 0:
    print("Number is positiv")
elif number < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")
# Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a==b:
    print("The number are equal")
else:
    print(min([a,b]), max([a,b]))
    