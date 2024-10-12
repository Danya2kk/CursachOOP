from abc import ABC, abstractmethod


class Service(ABC):
    def __init__(self, name, price, duration):
        self._name = name
        self._price = price
        self._duration = duration

    @abstractmethod
    @property
    def name(self):
        pass

    @abstractmethod
    @property
    def price(self):
        pass

    @abstractmethod
    @property
    def duration(self):
        pass

    @abstractmethod
    @name.setter
    def name(self, name):
        pass

    @abstractmethod
    @price.setter
    def price(self, price):
        pass

    @abstractmethod
    @duration.setter
    def duration(self, duration):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Haircut(Service):
    def __init__(self, price, duration, style):
        super().__init__("Haircut", price, duration)
        self._style = style

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def duration(self):
        return self._duration

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def style(self):
        return self._style

    def __str__(self):
        return f"{self.name}({self.style}): {self.price}$, {self.duration} минут"


class Manicure(Service):
    def __init__(self, price, duration, nails_type):
        super().__init__("Manicure", price, duration)
        self._nails_type = nails_type

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def duration(self):
        return self._duration

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def nails_type(self):
        return self._nails_type

    def __str__(self):
        return f"{self.name}({self.nails_type}): {self.price}$, {self.duration} минут"


class Pedicure(Service):
    def __init__(self, price, duration, nails_type):
        super().__init__("Pedicure", price, duration)
        self._nails_type = nails_type

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def duration(self):
        return self._duration

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def nails_type(self):
        return self._nails_type

    def __str__(self):
        return f"{self.name}({self.nails_type}): {self.price}$, {self.duration} минут"


class Facial(Service):
    def __init__(self, price, duration, type_facial):
        super().__init__("Facial", price, duration)
        self._type = type_facial

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def duration(self):
        return self._duration

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def type(self):
        return self._type

    def __str__(self):
        return f"{self.name}({self.type}): {self.price}$, {self.duration} минут"


class Massage(Service):
    def __init__(self, price, duration, style):
        super().__init__("Massage", price, duration)
        self._style = style

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def duration(self):
        return self._duration

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def style(self):
        return self._style

    def __str__(self):
        return f"{self.name}({self.style}): {self.price}$, {self.duration} минут"
