class Animal:
    def move(self):
        print("Harakatlanyapti ...")

class Bird(Animal):
    def move(self):
        print("Qush uchyapti")
    
class Fish(Animal):
    def move(self):
        print("Baliq suzyapti")
a1 = Bird()
a2 = Fish()

a1.move()
a2.move()