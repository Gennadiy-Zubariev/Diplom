from datetime import datetime


class Person:

    def __init__(self, first_name, birth_date, gender, last_name='',
                 patronymic='', death_date=''):
        if not first_name.strip():
            raise ValueError("Введіть ім'я")
        self.last_name = last_name.strip().capitalize() if last_name else None
        self.first_name = first_name.strip().capitalize()
        self.gender = self.gender_processing(gender)
        self.patronymic = patronymic.strip().capitalize() if patronymic else None
        self.birth_date = self.date_processing(birth_date)
        self.death_date = self.date_processing(death_date) if death_date else None


    def __str__(self):
        full_name = (
            f"{self.last_name if self.last_name else "Фамілія відсутня"} "
            f"{self.first_name} "
            f"{self.patronymic if self.patronymic else "По батькові відсутнє"}"
        )
        full_year_str = f"Повних {self.full_year} {self.word_full_year()}"
        gender_str = f"Стать - {"чоловіча" if self.gender == "m" else "жіноча"}"
        birth_date_str = f"{self.word_born()} - {self.birth_date.strftime("%d.%m.%Y")}"
        death_date_str = f"{self.word_dead()} - {self.death_date.strftime("%d.%m.%Y") if self.death_date else "---"}"
        return f"{full_name}\n{full_year_str}\n{gender_str}\n{birth_date_str}\n{death_date_str}"


    def __eq__(self, other):
        if isinstance(other, Person):
            return (
                    self.last_name == other.last_name and
                    self.first_name == other.first_name and
                    self.patronymic == other.patronymic and
                    self.birth_date == other.birth_date and
                    self.gender == other.gender
                    )


    @staticmethod
    def from_dictionary(data):
        try:
            return Person(
                last_name=data["last_name"] if data["last_name"] != '' else None,
                first_name=data["first_name"],
                patronymic=data["patronymic"] if data["patronymic"] != '' else None,
                gender=data["gender"],
                birth_date=data["birth_date"],
                death_date=data["death_date"] if data["death_date"] != '' else None
            )
        except ValueError:
            print("У файлі не заповнено обов'язкове поле")

    @property
    def full_year(self):
        end_date = self.death_date if self.death_date else datetime.today().date()
        age = end_date.year - self.birth_date.year
        if (end_date.month, end_date.day) < (self.birth_date.month,
                                             self.birth_date.day):
            age -= 1
        return age


    def date_processing(self, date_inp):
        formates = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"]
        for f in formates:
            try:
                return datetime.strptime(date_inp, f).date()
            except ValueError:
                continue
        raise ValueError("Невірний формат дати")

    def gender_processing(self, gender_inp):
        gender= gender_inp.strip().lower()
        genders = {"ч": "m", "ж": "f", "m": "m", "f": "f"}
        if gender in genders:
            return genders[gender]
        raise ValueError("стать повинна бути 'ч'/'ж' або 'm'/'f'")


    def word_full_year(self):
        if 11 <= self.full_year % 100 <= 14:
            return "років"
        elif self.full_year % 10 == 1:
            return "рік"
        elif 2 <= self.full_year % 10 <= 4:
            return "роки"
        else:
            return "років"

    def word_born(self):
        return "Народився" if self.gender == "m" else "Народилась"

    def word_dead(self):
        return "Помер" if self.gender == "m" else "Померла"

    def full_name_lower(self):
        return ''.join([
            self.first_name.lower(),
            (self.last_name or '').lower(),
            (self.patronymic or '').lower()
        ])


    def to_dictionary(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patronymic": self.patronymic,
            "full_year": self.full_year,
            "gender": self.gender,
            "birth_date": self.birth_date.strftime("%d.%m.%Y"),
            "death_date": self.death_date.strftime("%d.%m.%Y") if self.death_date else None
        }


if __name__ == "__main__":
    gena = Person("Геннадій", "20.08.1987", "ч", "Зубарєв", "Андрійович")
    nina = Person("Ніна", "21.08.1984", "ж", "Мєліхова", "Вікторівна")
    boris = Person("Боріс", "20.08.1989", "ч", "Ворон", "Петрович")
    vanbka = Person("Ванька", "01.01.1990", "ч", "Руський", "Іванович", "01/01/2025")


    a =  gena.full_year
    print(a)
