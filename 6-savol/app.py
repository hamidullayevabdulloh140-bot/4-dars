class Person:
    def __init__(self, age, password):
        self.__age = age
        self.__password = password
    @property
    def age(self):
        return self.__age
    def set_age(self, new_age, password):
        if password != self.__password:
            print("Parol noto'g'ri.")
        elif new_age < 0:
            print("Yosh manfiy bo'lishi mumkin emas.")
        else:
            self.__age = new_age
            print(f"Yosh yangilandi: {self.__age}")

person1 = Person(25,"abc123")
print("Hozirgi yosh:", person1.age)
person1.set_age(30,"abc123")
print("Yangi yosh:", person1.age)

