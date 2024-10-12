from service import *


class Order:
    def __init__(self):
        self._services = []

    def add_service(self, service):
        self._services.append(service)

    @property
    def services(self):
        return self._services

    @property
    def total_cost(self):
        return sum(service.price for service in self._services)

    @property
    def total_duration(self):
        return sum(service.duration for service in self._services)


class FemaleOrder(Order):
    def __init__(self):
        super().__init__()
        self._gender = "female"

    def add_service(self, service):
        if isinstance(service, Facial) or isinstance(service, Manicure) or isinstance(service, Massage) or isinstance(service, Pedicure):
            super().add_service(service)
        else:
            print("Данная услуга недоступна для женских заказов.")

    def clear_service(self):
        self._services.clear()


class MaleOrder(Order):
    def __init__(self):
        super().__init__()
        self._gender = "male"

    def add_service(self, service):
        if isinstance(service, Facial) or isinstance(service, Haircut) or isinstance(service, Massage):
            super().add_service(service)
        else:
            print("Данная услуга недоступна для мужских заказов.")

    def clear_service(self):
        self._services.clear()