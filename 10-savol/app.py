class Device:
    def __init__(self, serial_number):
        self.__serial_number = serial_number 

    def get_serial_number(self):
        return self.__serial_number

class Laptop(Device):
    def __init__(self, serial_number, brand):
        super().__init__(serial_number)
        self.brand = brand

class Tablet(Device):
    def __init__(self, serial_number, screen_size):
        super().__init__(serial_number)
        self.screen_size = screen_size

laptop = Laptop("LAP123456", "Dell")
tablet = Tablet("TAB987654", 10.5)

print("Laptop :", laptop.get_serial_number())
print("Planshet :", tablet.get_serial_number())
