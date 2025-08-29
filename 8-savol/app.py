class Vehicle:
    def __init__(self, fuel):
        self.__fuel = fuel

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, amount):
        if amount >= 0:
            self.__fuel = amount
        else:
            print("Yonilg‘i miqdori manfiy bo‘la olmaydi.")

class Car(Vehicle):
    def __init__(self, fuel, km):
        super().__init__(fuel)
        self.km = km

    def need(self, distance):
        return distance * self.km

class Truck(Vehicle):
    def __init__(self, fuel, km):
        super().__init__(fuel)
        self.km = km

    def need(self, distance):
        return distance * self.km

car = Car(50,0.07)
car1 = Truck(120,0.15)

print("Mashina 100km uchun yonilg‘i:", car.need(100))

