class Media:
    def play(self):
        print("")

class Audio(Media):
    def play(self):
        print("Qo'shiq aytyapti")

class Video(Media):
    def play(self):
        print("Video ko'ryapti")

m1 = Audio()
m2 = Video()

m1.play()
m2.play()