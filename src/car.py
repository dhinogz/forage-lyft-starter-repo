from .engine import Engine
from .battery import Battery

class Car:

    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

