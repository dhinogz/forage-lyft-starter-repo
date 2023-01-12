from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):

    @abstractmethod
    def needs_service(self):
        pass

class Spindler(Battery):

    def __init__(self, last_service_date: int) -> None:
        self.last_service_date = last_service_date
        self.check_time = 2 # years
        self.current_date = datetime.today().date()


    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + self.check_time
        )
        return service_threshold_date < self.current_date



class Nubbin(Battery):

    def __init__(self, last_service_date: int) -> None:
        self.last_service_date = last_service_date
        self.check_time = 4 # years
        self.current_date = datetime.today().date()


    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + self.check_time
        )
        return service_threshold_date < self.current_date
            