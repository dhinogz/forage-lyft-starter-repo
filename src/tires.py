from abc import ABC, abstractmethod


class Tires(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class Carigan(Tires):

    def __init__(self, tires_wear: list) -> None:
        if any(tire_wear > 1.0 for tire_wear in tires_wear):
            raise ValueError("Tire wear cannot be greater than 1.0")
        self.tires_wear = tires_wear

    def needs_service(self):
        return any(tire_wear >= 0.9 for tire_wear in self.tires_wear)


class Octoprime(Tires):

    def __init__(self, tires_wear: list) -> None:
        if any(tire_wear > 1.0 for tire_wear in tires_wear):
            raise ValueError("Tire wear cannot be greater than 1.0")
        self.tires_wear = tires_wear

    def needs_service(self):
        return sum(self.tires_wear) >= 3