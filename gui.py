import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog

from person import Person
from people_database import PeopleDatabase



db = PeopleDatabase()
db.read_from_file()

#############################ADD############################
def open_add_person_window():
    add_win = tk.Toplevel()
    add_win.title("Додати людину")
    add_win.geometry("400x400")
    add_win.configure(bg="white")

    fields = {}
    labels = ["Ім'я", "Прізвище", "По батькові", "Дата народження",
              "Дата смерті", "Стать (ч/ж, m/f)"]
    for i, label in enumerate(labels):
        tk.Label(add_win, text=label, bg="white").grid(row=i, column=0, padx=10, pady=5, sticky='e')
        entry = tk.Entry(add_win)
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
        except Exception as e:
            tk.messagebox.showerror("Помилка", str(e))

    tk.Button(add_win, text="Зберегти", command=save_person, bg="lightgreen").grid(
        row=len(fields), column=0, columnspan=2, pady=10
    )

##########################SAVE IN FILE###################################
def save_into_file():
    try:
        file_name = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Оберіть файл для збереження"
        )
        if not file_name:
            return  # Користувач натиснув "Скасувати"

        db.save_to_file(file_name)
        tk.messagebox.showinfo("Успіх", f"Дані збережено у файл:\n{file_name}")
    except Exception as e:
        tk.messagebox.showerror("Помилка", str(e))


##########################READ FROM FILE###################################


def download_from_a_file():
    file_path = filedialog.askopenfilename(
        title="Оберіть JSON-файл",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )

    if not file_path:
        return  # Користувач скасував вибір

    try:
        db.read_from_file(file_path)
        messagebox.showinfo("Успіх",
                            f"Файл '{file_path}' завантажено успішно!")
    except FileNotFoundError:
        messagebox.showerror("Помилка", f"Файл '{file_path}' не знайдено!")
    except Exception as e:
        messagebox.showerror("Помилка", f"Сталася помилка: {str(e)}")


##########################SHOW ALL###################################
def show_all():
    result_all = tk.Text(root, width=60, height=15, wrap="word")
    result_all.pack()


############################FIND############################
def open_find_person_window():

    find_win = tk.Toplevel()
    find_win.title("Пошук людини")
    find_win.geometry("600x600")
    find_win.configure(bg="gray")

    tk.Label(find_win, text="Введіть ім'я, або його частину", bg="red").grid(row=0, column=0, padx=10, pady=5, sticky='w')
    search_entry = tk.Entry(find_win,width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    result_text = tk.Text(find_win, width=60, height=15, wrap="word")
    result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def find_person():

        part_text = search_entry.get().strip()
        result_text.delete("1.0", tk.END)
        results = db.search_people_from_database(part_text)

        if not results:
            messagebox.showinfo("Нічого не знайдено")
        else:
            for person in results:
                result_text.insert(tk.END, f"{person}\n{'#' * 30}\n")



    tk.Button(find_win, text="Знайти", command=find_person, bg="lightgreen").grid(
        row=5, column=1, columnspan=2, pady=10
    )


##########################MAIN###############################
def main():
    root = tk.Tk()
    h = 500
    w = 600
    root.title("База даних людей")
    root.config(bg="gray")
    root.geometry(f"{h}x{w}+500+300")
    photo = tk.PhotoImage(file="img.png")
    root.iconphoto(False, photo)

    tk.Button(root, text="Додати людину", width=20, command=open_add_person_window).pack(pady=10)

    tk.Button(root, text="Зберегти у файл", width=20, command=save_into_file).pack(pady=10)

    tk.Button(root, text="Знайти людину", width=20,command=open_find_person_window).pack(pady=10)

    tk.Button(root, text="Завантажити з файла", width=20,command=download_from_a_file).pack(pady=10)

    # tk.Button(root, text="Показати всю базу", width=20,command=download_from_a_file).pack(pady=10)


    root.mainloop()

if __name__ == "__main__":
    main()

