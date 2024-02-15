from abc import ABC, abstractmethod

class Viechle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        pass


class Car(Viechle):
    def __init__(self, max_speed, current_speed):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def start_engine(self):
        return 'car started'

    def stop_engine(self):
        return 'car stopped'

class SportCar(Car):
    def __init__(self, max_speed, current_speed):
        super().__init__(max_speed, current_speed)

    def start_engine(self):
        return f'{Car.start_engine(self)}, and the max speed is {self.max_speed} '


    def stop_engine(self):
        self.current_speed = 0
        return f'{Car.stop_engine(self)}, and the current speed has decreased to {self.current_speed} '


car1 = Car(200,80)
# print(car1.current_speed)
# print(car1.max_speed)
# print(car1.start_engine())
# print(car1.stop_engine())

formula1 = SportCar(500,250)
# print(formula1.current_speed)
# print(formula1.max_speed)
# print(formula1.start_engine())
# print(formula1.stop_engine())