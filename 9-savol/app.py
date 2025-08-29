class Person:
    def __init__(self, national_id):
        self.__national_id = national_id  

    def get_national_id(self):
        return self.__national_id

class Student(Person):
    def __init__(self, national_id, name):
        super().__init__(national_id)
        self.name = name

    def check_id(self):
        national_id = self.get_national_id()
        return national_id.isdigit() and len(national_id) == 9

class Teacher(Person):
    def __init__(self, national_id, name):
        super().__init__(national_id)
        self.name = name

    def check_id(self):
        national_id = self.get_national_id()
        return national_id.isdigit() and len(national_id) == 9
student = Student("123456789", "Ali")
teacher = Teacher("987654321", "Guli")
print(f"Talaba: {student.check_id()}")
print(f"O‘qituvchi: {teacher.check_id()}")  
