from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def needs_service(self) -> None:
        pass


class Capulet(Engine):

    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000



class Willoughby(Engine):

    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000


class Sternman(Engine):

    def __init__(self, is_warning_light_on: bool) -> None:
        self.is_warning_light_on = is_warning_light_on

    def needs_service(self) -> bool:
        return self.is_warning_light_on
