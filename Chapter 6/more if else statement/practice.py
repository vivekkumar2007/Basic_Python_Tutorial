# for num in range (2,51):
#     prime = True
#     l=[]
#     for i in range(2,num):
#         if num%i==0 :
#             prime=False
#             break
#     if prime==False :
#         continue
#     print(num)
#q1
# for num in range (0,101):
#     num=int(input("Enter a integer:"))

#     if 90<=num<=100 :
#         print("Grade: A")
#     elif 80<=num<=89 :
#         print("Grade: B")
#     elif 70<=num<=79 :
#         print("Grade: C")
#     elif 60<=num<=69 :
#         print("Grade: D")
#     else: 
#         print("Grade:F")

# for i in range (1,101):
#     if i%3==0 and i%5==0 :
#         print ("FizzBuzz")
#         continue
#     if i%3==0:
#         print("Fizz")
#         continue
#     if i%5==0:
#         print("Buzz")
#         continue
    
#     print(i)

# def odd_even_no(numbers):
#     even_no=[]
#     odd_no=[]

#     for num in numbers:
#         if num%2==0:
#             even_no.append(num)
#         else:
#             odd_no.append(num)
#     return even_no , odd_no

    

# numbers=eval(input("Enter a list: "))

# even_no,odd_no=odd_even_no(numbers)

# print("even no:", even_no)
# print("odd no:", odd_no)
# def counts_vowel():
#     sentence=input("Enter a sentence:")
#     vowel='aeiouAEIOU'
#     vowel_count=0

#     for char in sentence:
#         if char in vowel:
#             vowel_count +=1
#     return vowel_count

# print("Total no of vowel in sentence:",counts_vowel())

def password_checker(password):

    is_digits=False
    is_uppercase=False 
    is_lowercase =False

    if len(password)<8:
        print("Invalid password!! password must contain atleast 8 character")
    if password.isdigit()==True:
        is_digits=True
    if password.isupper()==True:
        is_uppercase=True 
    if password.islower()==True:
        is_lowercase ==True
        
    if is_digits==True and is_uppercase==True and is_lowercase==True and len(password)>8 :
        print("Your password is successfully created and your password is :", password)
        
    if is_digits==False:
        print("Invalid password!!password must contain atleast one digit")
    elif is_uppercase==False:
        print("Invalid password!! password must contain atleast one uppercase alphabet")
    elif is_lowercase == False:
        print("Invalid passsword!!password must contain atleast one lowercase alphabet")

    if is_digits==True and is_uppercase==True and is_lowercase==True and len(password)>8 :
        print("Your password is successfully created and your password is :", password)
password=input("Enter your password: ")

 
password_checker(password)
   
   


                













    