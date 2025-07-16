from person import Person
from people_database import PeopleDatabase
import tkinter as tk


def say_hello():
    print("Hello")


def add_label():
    label = tk.Label(win, text="new")
    label.pack()


def counter():
    global coun
    coun += 1
    btn_4_counter["text"] = f"Counter: {coun}"


coun = 0

win = tk.Tk()
h = 500
w = 600
photo = tk.PhotoImage(file="img.png")
win.iconphoto(False, photo)
win.config(bg="gray")
win.title("База даних людей")
win.geometry(f"{h}x{w}+500+300")
win.minsize(300, 400)
win.maxsize(600, 800)
win.resizable(True, True)

label_1 = tk.Label(win,
                   text="Hello",
                   bg="red",
                   fg="white",
                   font=("Arial", 16, "bold"),
                   # padx=50,#розмір х відстань тексту від углів поля
                   # pady=100,#розмір х
                   width=20,  # висота та ширина у знаках
                   height=10,
                   anchor='n',  # форматує куди липне текст s w n o
                   relief=tk.SUNKEN,  # рельєф поля, кнопки
                   bd=10,  # ширина рельєфу поля, кнопки
                   justify=tk.LEFT  # вирівнювання тексту(багатострокового)
                   )

btn_1_say_hello = tk.Button(win,
                            text="Button1",
                            command=say_hello
                            )
btn_2_add_new = tk.Button(win,
                          text="Button2",
                          command=add_label
                          )

btn_3_add_new_lambda = tk.Button(win,
                                 text="Add new label",
                                 command=lambda: tk.Label(win,
                                                          text="New Lambda").pack()
                                 )

btn_4_counter = tk.Button(win,
                          text=f"Counter {coun}",
                          command=counter,
                          activebackground="blue",
                          activeforeground="white",
                          bg="red",
                          state=tk.NORMAL
                          )

label_1.pack()
btn_3_add_new_lambda.pack()
btn_1_say_hello.pack()
btn_2_add_new.pack()
btn_4_counter.pack()

win.mainloop()
# def open_window_to_download_from_a_file():
#     from_a_file_win = tk.Toplevel()
#     from_a_file_win.title("Завантаження з файлу")
#     from_a_file_win.geometry("600x600")
#     from_a_file_win.configure(bg="white")
#
#     tk.Label(from_a_file_win, text="Введіть ім'я файлу", bg="white").grid(
#         row=0, column=0, padx=10, pady=5, sticky='w')
#     search_entry = tk.Entry(from_a_file_win, width=30)
#     search_entry.grid(row=0, column=1, padx=10, pady=5)
# def download_from_a_file():
#     file_name = search_entry.get().strip()
#     if not file_name:
#         tk.messagebox.showerror("Помилка введення даних")
#         return
#
#     try:
#         db.read_from_file(file_name)
#     except FileNotFoundError:
#         tk.messagebox.showerror("Помилка",f"айл {file_name} не знайдено!")
#     except Exception as e:
#         messagebox.showerror("Помилка", f"Сталася помилка: {str(e)}")
#
# tk.Button(from_a_file_win, text="Завантажити", command=download_from_a_file, bg="lightgreen").grid(row=5, column=1, columnspan=2, pady=10)


# def save_into_file():
#     try:
#         db.save_to_file()
#         tk.messagebox.showinfo("Успіх", "Файл збережено успішно!")
#     except Exception as e:
#         tk.messagebox.showerror("Помилка", str(e))