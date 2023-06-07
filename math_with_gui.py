import math
import tkinter as tk
from tkinter import messagebox

def calculate_value():
    try:
        x = float(entry.get())
        if x >= 0:
            y = math.sqrt(x**3)
        else:
            y = math.log(abs(x))
        result_label.config(text="Результат: " + str(y))
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный Ввод. Введите числовое значение.")

# Васькова Алина Николаевна , варинант 5, группа 44-22-114
window = tk.Tk()
window.title("Расчет")
window.geometry("400x200")

input_label = tk.Label(window, text="Введите числовое значение:")
input_label.pack()
entry = tk.Entry(window)
entry.pack()

calculate_button = tk.Button(window, text="Рассчитать", command=calculate_value)
calculate_button.pack()

result_label = tk.Label(window, text="Вычисления:")
result_label.pack()


window.mainloop()