# Нужно написать программу,
# которая будет считывать со стандартного ввода целочисленные границы промежутка
# (сначала левая, потом правая, каждая на отдельной строке).
# А дальше будет считывать целые числа со стандартного ввода пока не встретит пустую строку,
# которая будет означать конец ввода.
# Нужно будет проверить входят ли все введенные числа в промежуток,
# проверка включает в себя границы промежутка.


# Считываем границы промежутка
left = int(input().strip())
right = int(input().strip())

# Считываем числа для проверки
numbers = []
while True:
    line = input().strip()
    if line == "":  # Проверяем на пустую строку
        break
    numbers.append(int(line))

# Проверяем, входят ли все числа в заданный промежуток
result = all(left <= num <= right for num in numbers)

# Выводим результат
print(result)