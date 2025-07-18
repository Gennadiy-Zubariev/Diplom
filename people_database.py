import pickle
from person import Person


class PeopleDatabase:

    def __init__(self):
        self.people_lst = []

    def add_person(self, person_obj):
        if person_obj in self.people_lst:
            raise ValueError("Така людина вже є у базі")
        else:
            self.people_lst.append(person_obj)

    def dell_person(self, *args):
        for person_obj in args:
            self.people_lst.remove(person_obj)

    def save_to_file(self, filename="people_data.pkl"):
        with open(filename, "wb") as file:
            pickle.dump([person for person in self.people_lst], file)
            print("Дані збережено у файл:", filename)

    def read_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                database = pickle.load(file)
                if database:
                    self.people_lst = [person for person in database]
                    print("Дані завантажено з файлу:", filename)
                else:
                    self.people_lst = []
        except FileNotFoundError:
            print("Файл не знайдено")
        except Exception as e:
            print(str(e))

    def search_people_from_database(self, search_word):
        return [
            people for people in self.people_lst
            if search_word.lower() in people.full_name_lower()
        ]

    def list_all(self):
        if not self.people_lst:
            raise ValueError("База порожня")
        return self.people_lst
