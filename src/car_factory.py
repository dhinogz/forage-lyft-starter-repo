from datetime import datetime

from .car import Car
from .engine import Capulet, Willoughby, Sternman
from .battery import Spindler, Nubbin


class CarFactory:

    @staticmethod
    def create_calliope(current_mileage: int, last_service_mileage: int, last_service_date: datetime):
        """
        Creates a car with a Capulet engine and a Spindler battery
        """
        engine = Capulet(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = Spindler(last_service_date=last_service_date)
        car = Car(engine=engine, battery=battery)

        return car

    @staticmethod
    def create_glissade(current_mileage: int, last_service_mileage: int, last_service_date: datetime) -> Car:
        """
        Creates a car with a Willoughby engine and a Spindler battery
        """
        engine = Willoughby(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = Spindler(last_service_date=last_service_date)
        car = Car(engine=engine, battery=battery)

        return car

    @staticmethod
    def create_palindrome(is_warning_light_on: bool, last_service_date: datetime) -> Car:
        """
        Creates a car with a Sternman engine and a Spindler battery
        """
        engine = Sternman(is_warning_light_on=is_warning_light_on)
        battery = Spindler(last_service_date=last_service_date)
        car = Car(engine=engine, battery=battery)

        return car

    @staticmethod
    def create_rorschach(current_mileage: int, last_service_mileage: int, last_service_date: datetime) -> Car:
        """
        Creates a car with a Willoughby engine and a Nubbin battery
        """
        engine = Willoughby(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = Nubbin(last_service_date=last_service_date)
        car = Car(engine=engine, battery=battery)

        return car

    @staticmethod
    def create_thovex(current_mileage: int, last_service_mileage: int, last_service_date: datetime) -> Car:
        """
        Creates a car with a Capulet engine and a Nubbin battery
        """
        engine = Capulet(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = Nubbin(last_service_date=last_service_date)
        car = Car(engine=engine, battery=battery)

        return car

    