import tkinter as tk
from tkinter import scrolledtext

# Глобальные переменные
g_key = ""
received_msg = ""

# Функция для отправки ключа
def Send_key(key):
    print(f"Sending key: {key}")  # Здесь можно добавить логику отправки ключа

# Функция для отправки сообщений
def Send(message):
    print(f"Sending message: {message}")  # Здесь можно добавить логику отправки

# Функция для получения сообщений
def Get_message():
    return "Received message"  # Здесь можно добавить логику получения

# Функция обработки кнопки Send
def send_message():
    global g_key
    message = message_input.get("1.0", tk.END).strip()
    key = key_input.get("1.0", tk.END).strip()

    if key:  # Если ключ не пустой, обновляем g_key
        g_key = key
        Send_key(g_key)  # Отправляем новый ключ

    elif not key and g_key:  # Если ключ пустой, используем g_key
        key = g_key

    if message and (key or g_key):  # Отправляем сообщение, если есть текст в сообщении
        Send(message)
        message_input.delete("1.0", tk.END)  # Очистка поля ввода сообщения
        key_input.delete("1.0", tk.END)      # Очистка поля ввода ключа

# Функция обработки кнопки Get Message
def get_message():
    global received_msg
    received_msg = Get_message()  # Сохраняем полученное сообщение в глобальную переменную
    output_box.configure(state='normal')
    output_box.insert(tk.END, received_msg + '\n')
    output_box.configure(state='disabled')

# Создание основного окна
root = tk.Tk()
root.title("Message and Key Sender")

# Поле для вывода сообщений
output_box = scrolledtext.ScrolledText(root, width=50, height=10, state='disabled')
output_box.pack(pady=10)

# Поле для ввода сообщения
message_label = tk.Label(root, text="Message:")
message_label.pack()
message_input = tk.Text(root, height=2)
message_input.pack(pady=5)

# Поле для ввода ключа
key_label = tk.Label(root, text="Key:")
key_label.pack()
key_input = tk.Text(root, height=2)
key_input.pack(pady=5)

# Кнопки
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=(10, 0))

get_button = tk.Button(root, text="Get Message", command=get_message)
get_button.pack(side=tk.LEFT, padx=(10, 0))

# Запуск интерфейса
root.mainloop()









