"""
Polymorphism:
 ---> When the same operator is allowed to have diffferent meaning according to the context.
"""
# print(1 + 2)   # 3
# print("Vivek" + ' Kumar')  # concatenate
# print([1,2,3] + [4,5,6])   # merge

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img= img
    def showNumber(self):
        print(self.real , "+", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

c1 = Complex(4,6)
c1.showNumber()
c2 = Complex(7,3)
c2.showNumber()

c3 = c1 + c2
c3.showNumber()
# c3 = c1.add(c2)
# c3.showNumber()


    