# When one class(child/derived) derives the properties & methods of another class(parent/base)
class Car:
    color = "White"

    @staticmethod
    def start():
        print("Car has started...")

    @staticmethod
    def stop():
        print("Car has stopped.")

class ToyotaCar(Car):    # It inherits all properties and method of Car class
    color = "black"

    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

car1.start()
print(car1.color)
