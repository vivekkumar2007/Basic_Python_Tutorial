# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         avg = sum(self.marks)/len(self.marks)
#         print(f"Hi {self.name}, Your avg score is: {avg}")

#     @staticmethod  # decorator
#     def college():    # it doesn't take self argument beacuse it is static method
#         print("IIT Mandi")

# s1 = student("Vivek Kumar", [98,94,89,89,84])
# s1.average()
# s1.college()

class Account:
    def __init__(self,balance, account_No):
        self.balance = balance
        self.AccNo= str(account_No)

    def debit(self,amount):
        self.balance = self.balance - amount
        print("You have successfully debited Rs",amount,"Now your available balance is",self.balance)

    def credit(self,amount):
        self.balance = self.balance + amount
        print("You have successfully credited Rs",amount,"Now your available balance is",self.balance)

    def get_balance(self):
        print(f"Your available balance with A/C No. xxxxx{self.AccNo[-4:]} is: Rs",self.balance)

acc1 = Account(10000, 123456789)
acc1.debit(5000)
acc1.credit(20000)
acc1.get_balance()