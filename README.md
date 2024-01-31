# oop
car class
class Car:
    def __init__(self, brand, model, production_year, color, horse_power):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = False

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def production_year(self):
        return self.__production_year

    @property
    def color(self):
        return self.__color

    @property
    def horse_power(self):
        return self.__horse_power

    @property
    def is_sport_car(self):
        return self.__is_sport_car

    def change_color(self, new_color):
        if self.__color != new_color:
            self.__color = new_color
            return True
        else:
            return False

    def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power += hp
            return True
        elif hp <= 0:
            return False


car1 = Car('opel', 'astra', 2019, 'green', 200)
print(car1.change_color('red'))
print(car1.color)
print(car1.increase_horse_power(100))
print(car1.horse_power)

car2 = Car('porsche', '911', 1994, 'red', 450)
print(car2.change_color('red'))
print(car2.color)
print(car2.increase_horse_power(-100))
print(car2.horse_power)
