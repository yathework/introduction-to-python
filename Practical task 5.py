# Необходимо написать программу,
# которая будет считывать три числа и выводить их в определенном формате.
# Первое число целое, второе с плавающей точкой, третье целое неотрицательное.
# По примерам необходимо определить требуемый формат данных.
#
# Пример 1
#
# Входные данные ➖ Выходные данные
# 102 ➖ +000000102
# 3.1415926535 ➖ ######3.14
# 1127 ➖ 0000_0100_0110_0111
#
# Пример 2
#
# Входные данные ➖ Выходные данные
# -1024 ➖ -000001024
# -123.7 ➖ ###-123.70
# 65535 ➖ 1111_1111_1111_1111



# Считываем три числа из стандартного ввода
integer1 = int(input().strip())       # Первое число: целое (например, 102 или -1024)
float1 = float(input().strip())       # Второе число: с плавающей точкой (например, 3.141592 или -123.7)
integer2 = int(input().strip())       # Третье число: целое неотрицательное (например, 1127 или 65535)

# Форматируем первое число: выводим с обязательным знаком (+ или -), дополненным нулями до 10 символов
formatted_int1 = f"{integer1:+010}"

# Форматируем второе число: плавающее, ширина 10 символов, 2 знака после запятой
if float1 < 0:
    # Для отрицательных чисел заменяем пробелы на '#' перед числом
    formatted_float1 = f"{float1:10.2f}".replace(" ", "#")
else:
    # Для положительных чисел заменяем пробелы на '#' перед числом
    formatted_float1 = f"{float1:10.2f}".replace(" ", "#")

# Форматируем третье число: представляем в виде двоичного числа из 16 символов, разделённого на блоки по 4 символа с помощью "_"
formatted_int2 = "_".join(f"{integer2:016b}"[i:i+4] for i in range(0, 16, 4))

# Выводим отформатированные результаты
print(formatted_int1)  # Первое число: форматированное целое
print(formatted_float1)  # Второе число: форматированное число с плавающей точкой
print(formatted_int2)  # Третье число: двоичное представление с разделителями "_"