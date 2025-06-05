# class student:
#     colllege_name = "IIT Mandi"   # Class Attributes
#     name = "anonymous"   # if class attr and obj attr have same name then object attr has higher priority.

#     def __init__(self,fullName, Roll_Number):  # __init__ function is callled as Constructor. It is automatically Invoked when object is created
#         self.name = fullName     # Instance Attributes/ obj attr
#         self.roll_number = Roll_Number
#         print("adding a new student in Database..")

# s1 = student("Vivek Kumar", "B24473")    # creating an object of class student with name s1.
# print(s1.name,s1.roll_number, s1.colllege_name)

# s2 = student("Nirbhik Viswas", "B24450")
# print(s2.name,s2.roll_number)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# Car1 = Car()
# print(Car1.color)
# print(Car1.brand)

# Car2 = Car()
# print(Car2.color)
# print(Car2.brand)

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def greeting(self):   # it is called as method in Class, i.e function in class is called method
        print("Welcome Student,",self.name )

    def get_marks(self):
        return self.marks

s1 = Student("Vivek Kumar",98)
s1.greeting()
print(s1.get_marks())