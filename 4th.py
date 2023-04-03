import math
import random

operation = input("Выберите операцию (+, -, /, *, **, mod, rand, !, acos): ")

if operation in ["+", "-", "/", "*", "**", "mod"]:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "**":
        result = num1 ** num2
    elif operation == "mod":
        result = num1 % num2
    
    print("Результат: ", result)

elif operation == "rand":
    lower = float(input("Введите нижнюю границу: "))
    upper = float(input("Введите верхнюю границу: "))
    
    result = random.uniform(lower, upper)
    
    print("Результат: ", result)

elif operation == "!":
    num = int(input("Введите число: "))
    
    result = math.factorial(num)
    
    print("Результат: ", result)

elif operation == "acos":
    num = float(input("Введите число: "))
    
    if num < -1 or num > 1:
        print("Ошибка: аргумент должен быть между -1 и 1")
    else:
        result = math.acos(num)
        print("Результат: ", result)
        
else:
    print("Ошибка: неверная операция")
