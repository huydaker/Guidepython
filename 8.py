import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Python GUI")

label_name = tk.Label(window, text="Enter your name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(window)
entry_name.grid(row=1, column=0, padx=10, pady=10)

label_number = tk.Label(window, text="Choose a number:")
label_number.grid(row=0, column=1, padx=10, pady=10)

combo = ttk.Combobox(window, values=[1, 2, 4, 42, 100])
combo.grid(row=1, column=1, padx=10, pady=10)
combo.current(0)  #set giá trị mặc định

#hàm xử lý khi nhấn nút
def on_click():
    name = entry_name.get()  #lấy tên từ Entry
    number = combo.get()  #lấy số từ ComboBox
    button.config(text=f"Hello {name} {number}")

button = tk.Button(window, text="Click Me!", command=on_click)
button.grid(row=1, column=2, padx=10, pady=10)

window.mainloop()
