# # from for loop
# n=int(input("Enter the number: "))
# for i in range(1,11):
#      print(n,'X',i,"=",n*i)

# # from while loop
# i=1
# while i<=10:
#     print (f"{n}X{i}={i*n}")
#     i+=1
 
# n=int(input("Enter the number: "))
# for i in range(10,0,-1):
#      print(n,'X',i,"=",n*i)

# greeting if name in teh 
# l1=["Harry", "Sohan","Sachin", "Rahul", "Satyam", "Avanish"]
# for name in l1:
#     if name.find('S')==0 :
#         print("Good Morning,",name+'!')

# finding a given number is prime or not
# # method 1
# n=int(input("Enter the number: "))
# divisor=[]
# for i in range(1,n+1):
#     if (n%i)==0 :
#         divisor.append(i) 
# print(divisor)        
# if len(divisor)==2 :
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")

# #method 2 
# n=int(input("Enter the number: "))
# prime=True
# for i in range(2,n):
#     if (n%i)==0 :
#         prime=False 
#         break        
# if prime==True:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")

# sum of n natural number using while loop
# n=int(input("Enter the number: "))
# sum=0
# i=1
# while i<=100 :
#     sum+=i
#     i+=1
# print(sum)

# Calculating factorial of n using for loop
# n=int(input("Enter the number: "))
# factorial=1
# for i in range (1,n+1):
#     factorial *=i
# print(f"factorial of {n} is {factorial}")

#printing a inverted v of *'s
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i) + (2*i-1)*"*" + " "*(n-i))


#pritning star in corner only
n=int(input("Enter the number: "))
for i in range(1,n+1):
    if 1<i<n :
        print("*" + " "*(n-2) + "*")
    else:
        print("*"*n)


