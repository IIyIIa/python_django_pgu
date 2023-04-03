string = input("Введите произвольную строку: ")
string_length = len(string)

for i in range(string_length):
    if i == 2:
        continue
    if string[i] == "c":
        print("В строке есть символ 'c'")
    print(string[i], end="")

print("\nДлина строки:", string_length)
print("Строка без последнего символа:", string[:-1])
