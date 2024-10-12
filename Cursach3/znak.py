class ZNAK:
    def __init__(self, surname, name, zodiac_sign, birth_date):
        self._surname = surname
        self._name = name
        self._zodiac_sign = zodiac_sign
        self._birth_date = birth_date  # список из трех элементов: [день, месяц, год]

    def __str__(self):
        return f"{self._surname} {self._name}, Знак зодиака: {self._zodiac_sign}, Дата рождения: {'.'.join(map(str, self._birth_date))}"

    def get_surname(self):
        return self._surname

    def get_name(self):
        return self._name

    def get_zodiac_sign(self):
        return self._zodiac_sign

    def get_birth_date(self):
        return self._birth_date