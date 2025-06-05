# # q1
# myDict={"Ghadi":"Watch",
#         "Pankha":"Fan",
#         "Namaste":"Hello",
#         "Duniya":"world",
#         "Maidan":"Field",
#         "Aadami":"Man"}

# print("Options are", list(myDict.keys()))
# a = input("Ek shabd likhen: ")
# # Below line will not throw an error if the key is not present in the dictionary
# print("aapake shabd ka English me rupantran:",myDict.get(a))

# # q2
# s=set()
# for i in range (1,9):
#     a=int(input("Enter a number:"))
#     s.add(a)
# print(s)

# q3
myDict={}
f1=input("Enter your name:")
l1=input("Enter your favourite language:")
f2=input("Enter your name:")
l2=input("Enter your favourite language:")
f3=input("Enter your name:")
l3=input("Enter your favourite language:")
f4=input("Enter your name:")
l4=input("Enter your favourite language:")

updatedDict={f1 : l1,
             f2:l2,
             f3:l3,
             f4:l4}
myDict.update(updatedDict)
print(myDict)























