number = float(input("Введите произвольное число: "))
boundary = float(input("Введите пограничное число: "))

if number < boundary:
    print("Введенное число меньше пограничного числа")
elif number > boundary:
    print("Введенное число больше пограничного числа")
    if number > boundary * 3:
        print("Введенное число больше пограничного более, чем в 3 раза")
else:
    print("Введенное число равно пограничному числу")
