# class student:
#     def __init__(self,name):
#         self.name = name

# s1 = student("Vivek")
# print(s1.name)

# del s1.name     
# print(s1.name) 

class Account:
    def __init__(self,acc_no, acc_password):
        self.acc_no = acc_no
        self.__acc_password = acc_password   # now __acc_password is private attributes it can't be accessed outside of class

    def show_password(self):
        print("Your password is:", self.__acc_password)  # it is accessed here because it is within the scope of class

acc1 = Account(12345, "abcde")
print(acc1.acc_no)
# print(acc1.__acc_password)   # It give error because __acc_passeword is private
acc1.show_password()