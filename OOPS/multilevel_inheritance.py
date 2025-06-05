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

    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
print(car1.color)
car1.start()

# multiple Inheritance

class A:
    VarA = "Welcome to class A."

class B:
    VarB = "Welcome to class B."

class C(A,B):
    VarC = "Welcome to class C."

wel = C()
print(wel.VarC)
print(wel.VarB)  
print(wel.VarA)