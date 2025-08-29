class Transport:
    def capacity(self):
        print("Transport ... ketyapti")
    
class Bus(Transport):
    def capacity(self):
        print("Avtobus Namanganga ketyapti ... ")

class Train(Transport):
    def capacity(self):
        print("Poyezd qayergadir ketyapti ...")

t1 = Bus()
t2 = Train()

t1.capacity()
t2.capacity()