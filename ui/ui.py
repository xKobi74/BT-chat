import tkinter as tk
from tkinter import scrolledtext

# Функция для отправки сообщений
def Send(message):
    print(f"Sending message: {message}")  # Здесь можно добавить логику отправки

# Функция для получения сообщений
def Get_message():
    return "Received message"  # Здесь можно добавить логику получения

# Функция обработки кнопки Send
def send_message():
    message = input_box.get("1.0", tk.END).strip()
    if message:
        Send(message)
        input_box.delete("1.0", tk.END)  # Очистка поля ввода

# Функция обработки кнопки Get Message
def get_message():
    received_message = Get_message()
    output_box.configure(state='normal')
    output_box.insert(tk.END, received_message + '\n')
    output_box.configure(state='disabled')

# Функция для обработки нажатия клавиши
def on_enter(event):
    send_message()

# Функция для управления фокусом и вызова клавиатуры
def focus_input(event):
    input_box.focus_set()  # Установка фокуса на поле ввода
    input_box.tkraise()    # Поднимаем поле ввода на передний план
    root.tkraise()         # Убедимся, что главное окно на переднем плане

# Функция для скрытия клавиатуры
def unfocus(event):
    input_box.quit()  # Убираем фокус с поля ввода, чтобы скрыть клавиатуру

# Создание основного окна
root = tk.Tk()
root.title("Message Sender/Receiver")

# Поле для вывода сообщений
output_box = scrolledtext.ScrolledText(root, width=50, height=10, state='disabled')
output_box.pack(pady=10)

# Поле для ввода сообщений
input_box = tk.Text(root, height=2)
input_box.pack(pady=10)
input_box.bind("<Return>", on_enter)  # Связываем нажатие клавиши Enter с функцией

# Обработка нажатий по экрану
root.bind("<Button-1>", focus_input)  # Фокус на поле ввода при нажатии
root.bind("<FocusOut>", unfocus)  # Убираем фокус при нажатии вне поля ввода

# Кнопки
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=(10, 0))

get_button = tk.Button(root, text="Get Message", command=get_message)
get_button.pack(side=tk.LEFT, padx=(10, 0))

# Запуск интерфейса
root.mainloop()




