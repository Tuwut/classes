import math
import sys
# Васькова Алина Николаевна , варинант 5, группа 44-22-114
def convert_value(x):
    if x >= 0:
        y = math.sqrt(x**3)
    else:
        y = math.log(abs(x))
    return y

try:
    x = float(input("Введите числовое значение: "))
    result = convert_value(x)
    print("Результат:", result)
except ValueError:
    print("Неверный Ввод. Введите числовое значение.")