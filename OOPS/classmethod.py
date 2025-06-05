# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("Hello Person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# # p1.__hello()  # It gives error because __hello() function is private now
# p1.welcome()


"""
CLASS METHOD
 ---> A class method is bound to the class & recieves the class as an implicit first argument.
 ---> static method can't access or modify class state & generallly for utility.
"""
class Person:
    name = "anonymous"

    # def changeName(self, name):
        # self.name = name          # it doesn't change the name of class attribute
        # Person.name = name          # it changes the clas attributes name
        # self.__class__.name = name  # it also changes the clas attributes name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)



 