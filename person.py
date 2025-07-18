from datetime import datetime


class Person:

    def __init__(self, last_name, first_name, birth_date, gender,
                 patronymic='', death_date=''):

        if not first_name.strip():
            raise ValueError("Ім'я є обов'язковим полем")
        self.first_name = first_name.strip().capitalize()
        if not last_name.strip():
            raise ValueError("Прізвище є обов'язковим полем")
        self.last_name = last_name.strip().capitalize()
        self.patronymic = patronymic.strip().capitalize() if patronymic else None
        self.birth_date = self.data_processing(birth_date, "birth")
        self.death_date = self.data_processing(death_date,
                                               "death") if death_date else None
        if not gender.strip():
            raise ValueError("Стать є обов'язковим полем")
        self.gender = self.gender_processing(gender)

    def __str__(self):
        full_name = (
            f"{self.first_name} "
            f"{self.last_name} "
            f"{self.patronymic if self.patronymic else ""}"
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

    @property
    def full_year(self):
        end_date = self.death_date if self.death_date else datetime.today().date()
        age = end_date.year - self.birth_date.year
        if (end_date.month, end_date.day) < (self.birth_date.month,
                                             self.birth_date.day):
            age -= 1
        return age

    def format_date_processing(self, date_inp):
        if not date_inp.strip():
            return None
        formates = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"]
        for f in formates:
            try:
                return datetime.strptime(date_inp, f).date()
            except ValueError:
                continue
        raise ValueError("Невірний формат дати")

    def data_processing(self, date_inp, death_or_birth):
        if not date_inp.strip() and death_or_birth == "birth":
            raise ValueError("Дата народження є обов'язковою")
        if not date_inp.strip() and death_or_birth == "death":
            return None
        date = self.format_date_processing(date_inp)
        if death_or_birth == "birth" and date > datetime.today().date():
            raise ValueError("Дата народження не може бути в майбутньому")
        elif death_or_birth == "death":
            if date and date > datetime.today().date():
                raise ValueError("Дата смерті не може бути в майбутньому")
            if date and date < self.birth_date:
                raise ValueError(
                    "Дата смерті не може бути раніше дати народження")
        return date

    def gender_processing(self, gender_inp):
        gender = gender_inp.strip().lower()
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
