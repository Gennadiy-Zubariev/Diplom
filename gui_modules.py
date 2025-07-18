import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter import ttk
import pickle

from person import Person
from people_database import PeopleDatabase


db = PeopleDatabase()


#############################ADD############################
def open_add_person_window():
    add_win = tk.Toplevel()
    add_win.title("Додати людину")
    add_win.geometry("400x400+350+300")
    add_win.configure(bg="#CCE5FF")
    add_win.resizable(False, False)

    '''Стилі кнопок'''
    style = ttk.Style(add_win)
    style.theme_use("clam")
    style.configure("Green.TButton", font=("Arial", 12), padding=10,
                    background="#99CCFF")
    style.map("Green.TButton", background=[("active", "#99FF99")])


    fields = {}
    labels = ["Ім'я", "Прізвище", "По батькові", "Дата народження",
              "Дата смерті", "Стать (ч/ж, m/f)"]
    for i, label in enumerate(labels):
        tk.Label(add_win, text=label, font=("Arial", 12, "bold"), fg="#0080FF",
             bg="#CCE5FF").grid(
            row=i, column=0, padx=10, pady=5, sticky='e')
        entry = tk.Entry(add_win, font=("Arial", 12), width=20)
        entry.grid(row=i, column=1, padx=10, pady=5)
        fields[label] = entry

    def save_person():
        try:
            person = Person(
                first_name=fields["Ім'я"].get(),
                last_name=fields["Прізвище"].get(),
                patronymic=fields["По батькові"].get(),
                birth_date=fields["Дата народження"].get(),
                death_date=fields["Дата смерті"].get(),
                gender=fields["Стать (ч/ж, m/f)"].get()
            )

            db.add_person(person)
            tk.messagebox.showinfo("Успіх", "Людину додано успішно!")
            add_win.destroy()
        except ValueError as e:
            tk.messagebox.showerror("Помилка!!!!", str(e))
        except Exception as e:
            tk.messagebox.showerror("Помилка", str(e))

    ttk.Button(add_win, text="Зберегти", command=save_person, style="Green.TButton", width=20).grid(sticky="ew", columnspan=2, padx=100)


############################FIND############################
def open_find_person_window():
    find_win = tk.Toplevel()
    find_win.title("Пошук людини")
    find_win.geometry("500x500+250+300")
    find_win.configure(bg="#CCE5FF")

    '''Стилі кнопок'''
    style = ttk.Style(find_win)
    style.theme_use("clam")
    style.configure("Green.TButton", font=("Arial", 12), padding=10,
                    background="#99CCFF")
    style.map("Green.TButton", background=[("active", "#99FF99")])
    style.configure("Red.TButton", font=("Arial", 12), padding=10,
                    background="lightcoral")
    style.map("Red.TButton",
              background=[("active", "red"), ("disabled", "lightgray")])

    tk.Label(find_win, text="Введіть ім'я, або його частину",
             font=("Arial", 12, "bold"), fg="#0080FF",
             bg="#CCE5FF").grid(
             row=0, column=0, padx=10, pady=5, sticky='w')
    search_entry = tk.Entry(find_win, width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    result_text = tk.Text(find_win, width=60, height=15, wrap="word")
    result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    delete_button = ttk.Button(find_win, text="Видалити", state="disabled",
                              style="Red.TButton", width=20)
    delete_button.grid(row=4, column=0,sticky="ew", columnspan=2, padx=100, pady=20)

    def find_person():

        part_text = search_entry.get().strip()
        result_text.delete("1.0", tk.END)
        results = db.search_people_from_database(part_text)

        if not results:
            messagebox.showinfo("Нічого не знайдено")
            delete_button.config(state="disabled")
        else:
            for person in results:
                result_text.insert(tk.END, f"{person}\n{'#' * 30}\n")


##########################DELETE PERSON###############################
            def delete_find_person():
                try:
                    if not results:
                        messagebox.showerror("Помилка", "База пуста")
                        return
                    db.dell_person(*results)
                    tk.messagebox.showinfo("Успіх", "Людину видалено успішно!")
                    result_text.delete("1.0", tk.END)
                    delete_button.config(state="disabled")
                except Exception as e:
                    messagebox.showerror("Помилка", str(e))

            delete_button.config(state="normal",
                                 command=delete_find_person)

    ttk.Button(find_win, text="Знайти", command=find_person,
              style="Green.TButton", width=20).grid(row=3, column=0, sticky="ew", columnspan=2, padx=100, pady=20)


##########################SHOW ALL###################################
def open_show_all_window():
    show_all_win = tk.Toplevel()
    show_all_win.title("Вся база")
    show_all_win.geometry("500x600+250+300")
    show_all_win.configure(bg="#CCE5FF")

    result_text = tk.Text(show_all_win, width=60, height=35, wrap="word")
    result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    try:
        all_data = db.list_all()
        for person in all_data:
            result_text.insert(tk.END, f"{person}\n{'#' * 30}\n")
    except ValueError as e:
        messagebox.showinfo("Увага", str(e))


##########################SAVE IN FILE###################################
def save_into_file():
    try:
        file_name = filedialog.asksaveasfilename(
            defaultextension=".pkl",
            filetypes=[("pkl files", "*.pkl")],
            title="Оберіть файл для збереження"
        )
        if not file_name:
            return

        db.save_to_file(file_name)
        tk.messagebox.showinfo("Успіх", f"Дані збережено у файл:\n{file_name}")
    except Exception as e:
        tk.messagebox.showerror("Помилка", str(e))


##########################READ FROM FILE###################################
def download_from_a_file():
    file_path = filedialog.askopenfilename(
        title="Оберіть pkl-файл",
        filetypes=[("pkl files", "*.pkl"), ("All files", "*.*")]
    )

    if not file_path:
        return

    try:
        db.read_from_file(file_path)
        messagebox.showinfo("Успіх",
                            f"Файл '{file_path}' завантажено успішно!")
    except Exception as e:
        messagebox.showerror("Помилка", f"Сталася помилка: {str(e)}")





