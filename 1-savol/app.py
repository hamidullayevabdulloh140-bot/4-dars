class Employee:
    def work(self):
        print("Xodim ishlayapti ...")

class Manager(Employee):
    def work(self):
        print("Menejir boshqaryapti ...")

class Devaloper(Employee):
    def work(self):
        print("Dasturchi kod yozyapti ...")

e1 = Manager()
e2 = Devaloper()

e1.work()
e2.work()
