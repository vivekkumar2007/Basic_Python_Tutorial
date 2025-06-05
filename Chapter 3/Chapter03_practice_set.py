#1
# user_name=input("Enter your name: ")
# greeting="Good Afternoon"
# print(user_name + ", " + greeting)

#2
# letter= '''Dear <|NAME|> ,
# You are selected

# <|DATE|> '''

# name= input("Enter your name:\n")
# date=input("Enter Date:\n")

# letter=letter.replace("<|NAME|>",name)
# letter=letter.replace("<|DATE|>",date)
# print(letter)

# #3
# string="This is the string  with double  spaces"
# c=string.find("  ")
# if c==-1:
#     print("This string has not double spaces")
# else:
#     print("This string has double spaces ")

# if c!=-1:
#     print(string.replace("  "," "))
# else:
#     pass

# string = "I love programming and programming is fun"
# old_word = "programming"
# new_word = "coding"
# i=0
# result=''
# while i<len(string):
#     if string[i:i+len(old_word)]==old_word:
#         result += new_word
#         i += len(old_word)
#     else:
#         result +=string[i]
#         i+=1
# print(result)

# print('cat'<'rat')

# def swap(x,y):
#     x=x-y
#     y=x+y
#     x=y-x
#     return x,y
# print(swap(-54,59))

# def Isdigit(myString):
#     digit='0123456789'
#     operator='-+'
#     for char in myString:
#         if char[0] in operator:
#             return True
#         elif char not in digit:
#             return False
        

# myString=input("Enter a integer:")
# while Isdigit(myString)==False:
#     myString=input("Don't think me fool, pls give a integer: ")
# print('Thanks for giving me Integer', myString)
    
# with open( r"C:\Users\vivek\input.txt" ) as f :
#     for line in f:
#         print(line.strip())