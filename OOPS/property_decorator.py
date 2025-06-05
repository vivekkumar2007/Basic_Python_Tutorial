# class Student:
#     def __init__(self, phy, chem, math):
#         self.physics = phy
#         self.chemistry = chem
#         self.mathematics = math
#         self.percentage = str((phy + chem + math)/3) + "%"

#     def Percentage(self):
#         self.percentage = str((self.physics + self.chemistry + self.mathematics)/3) + "%"

# stu1 = Student(97,89,93)
# print(stu1.percentage)

# stu1.physics = 90
# stu1.Percentage()   # if we don't use this then percentage will not change
# print(stu1.percentage)

"""
Property
 ---> We use @property decorator on any method in the class to use the method as a property.

"""
class Student:
    def __init__(self, phy, chem, math):
        self.physics = phy
        self.chemistry = chem
        self.mathematics = math

    @property
    def percentage(self):
        return str((self.physics + self.chemistry + self.mathematics)/3) + "%"

stu1 = Student(97,89,93)
print(stu1.percentage)

stu1.physics = 90
# No need to use this because we use property manager
# stu1.Percentage() 
print(stu1.percentage)
