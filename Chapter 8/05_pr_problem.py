# finding the gratest number of  three number
# def greatest(a,b,c):
#     if a>b:
#         f1=a
#     else:
#         f1=b 
#     if f1>c :
#         max=f1
#     else:
#         max=c
#     return max
# (a,b,c)=(2,5,3)
# print(f"gratest number among {a}, {b} and {c} is",greatest(a,b,c))

# Converting celsius to fahrenheit
# def celsius_to_fahrenheit(C):
#     F=(9/5)*C + 32
#     print("the temprature in fahrenheit is =", F)
#     return F
# celsius_to_fahrenheit(37) 

# writing a program to give sum of n natural number
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n + sum(n-1)
# print(sum(100))

# printing star's using function 
# def star(n):
#     for i in range (1,n+1):
#         pattern=((n+1-i)*"*" + (i-1)*" ")
#         print(pattern)
    
# star(4)

# removig a word in a string and strip at the same time

def remove_and_split(string, word):
    newStr = string.replace(word,"")
    return newStr.strip()

this= "    Vivek is a good boy    "
n= remove_and_split(this, "Vivek")
print(n)