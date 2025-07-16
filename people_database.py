import json
from person import Person


class PeopleDatabase:

    def __init__(self):
        self.people_lst = []

    def add_person(self, person_obj):
        if person_obj in self.people_lst:
            raise ValueError("Така людина вже є у базі")
        else:
            self.people_lst.append(person_obj)

    def dell_person(self, person_obj):
        if person_obj in self.people_lst:
            self.people_lst.remove(person_obj)
        else:
            print("Такої людини немає у базі")

    def save_to_file(self, filename="people_data.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([p.to_dictionary() for p in self.people_lst], file,
                      ensure_ascii=False, indent=1)
            print("Дані збережено у файл:", filename)

    def read_from_file(self, filename="people_data.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                database = json.load(file)
                self.people_lst = [Person.from_dictionary(data) for data in
                                   database]
            print("Дані завантажено з файлу:", filename)
        except FileNotFoundError:
            print("Файл не знайдено")

    def search_people_from_database(self, search_word):
        return [
            people for people in self.people_lst
            if search_word.lower() in people.full_name_lower()
        ]


    def list_all(self):
        if not self.people_lst:
            print("База порожня.")
        for i, person in enumerate(self.people_lst, 1):
            print(f"{i}:\n{person}\n{'-' * 30}")

if __name__ == "__main__":
    base = PeopleDatabase()

    gena = Person("Геннадій", "20.08.1987", "ч", "Зубарєв", "Андрійович")
    base.add_person(gena)
    nina = Person("Ніна", "21.08.1984", "ж", "Мєліхова", "Вікторівна")
    base.add_person(nina)
    boris = Person("Боріс", "20.08.1989", "ч", "Ворон", "Петрович")
    base.add_person(boris)
    vanbka = Person("Ванька", "01.01.1990", "ч", "Руський", "Іванович", "01/01/2025")
    base.add_person(vanbka)
    # base.read_from_file()
    # base.dell_person(gena)

    base.save_to_file()
    # for i in base.search_people_from_database('ге'):
    #     base.dell_person(i)
    # base.save_to_file()


    # base.dell_person(boris)
    # base.dell_person(vanbka)

    # gena = Person("Геннадій", "20.08.1987", "ч")
    # base.add_person(gena)

    # base.read_from_file()
    # nina = Person("Ніна", "21 08 1984", "ж", "Мєліхова", "Вікторівна")
    # base.add_person(nina)
    # base.list_all()
    # base.save_to_file()


    # for b in base.search_people_from_database('sd'):
    #     print(b)
