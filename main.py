import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter import ttk
import pickle

from person import Person
from people_database import PeopleDatabase
from gui_modules import *


# db.read_from_file()


def main():
    root = tk.Tk()
    h = 400
    w = 400
    root.title("Hillel Python Basik. Diplom Zubarev Gena")
    root.config(bg="#CCE5FF")
    root.geometry(f"{h}x{w}+750+300")
    root.resizable(False, False)

    photo = tk.PhotoImage(file="img.png")
    root.iconphoto(False, photo)

    '''Сітка для головного вікна'''
    root.grid_columnconfigure(0, weight=1)

    '''Стиль для кнопок'''
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Custom.TButton", font=("Arial", 12, "bold"), padding=10,
                    background="#99CCFF")
    style.map("Custom.TButton", background=[("active", "#99FF99")])

    '''Заголовок'''
    title_label = tk.Label(
        root,
        text="База даних людей",
        font=("Arial", 20, "bold"),
        fg="#0080FF",
        bg="#CCE5FF"
    )
    title_label.grid(row=0, column=0, pady=(20, 10))

    add = ttk.Button(root, text="Додати людину",
                     command=open_add_person_window, width=20,
                     style="Custom.TButton")
    find = ttk.Button(root, text="Знайти людину",
                      command=open_find_person_window, width=20,
                      style="Custom.TButton")
    show = ttk.Button(root, text="Показати всю базу",
                      command=open_show_all_window, width=20,
                      style="Custom.TButton")
    save = ttk.Button(root, text="Зберегти у файл", command=save_into_file,
                      width=20, style="Custom.TButton")
    load = ttk.Button(root, text="Завантажити з файла",
                      command=download_from_a_file, width=20,
                      style="Custom.TButton")

    add.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
    find.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
    show.grid(row=3, column=0, pady=10, padx=20, sticky="ew")
    save.grid(row=4, column=0, pady=10, padx=20, sticky="ew")
    load.grid(row=5, column=0, pady=10, padx=20, sticky="ew")

    root.mainloop()


if __name__ == "__main__":
    main()
