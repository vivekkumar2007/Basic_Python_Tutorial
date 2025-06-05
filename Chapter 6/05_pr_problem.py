# num1=int(input("Enter first number:"))
# num2=int(input("Enter 2nd number:"))
# num3=int(input("Enter 3rd number:"))
# num4=int(input("Enter 4th number:"))
# # 1st method
# if (num1 >= num2 and num1 >=num3 and num1 >=num4) :
#     print("The gratest number is =",num1)
# elif (num2 >= num1 and num2 >=num3 and num2 >=num4) :
#     print("The gratest number is =",num2)
# elif (num3 >= num2 and num3 >=num1 and num3 >=num4) :
#     print("The gratest number is =",num3)
# else:
#     print("The gratest number is =",num4)

# # 2nd method
# if num1>num2 :
#     f1 = num1
# else:
#     f1 = num2

# if num3>num4 :
#     f2 = num3
# else:
#     f2 = num4

# if f1 > f2 :
#     print("the greatest number is",f1)
# else:
#     print("the greatest number is",f2)
# s1_maxmarks=100
# s2_maxmarks=100
# s3_maxmarks=100
# s1_marks=int(input("enter your s1_marks: "))
# s2_marks=int(input("enter your s2_marks: "))
# s3_marks=int(input("enter your s3_marks: "))

# if (s1_marks + s2_marks + s3_marks)>=(s1_maxmarks+s2_maxmarks+s3_maxmarks)*.4 :
#     if s1_marks>=(s1_maxmarks)*(33/100) and s2_marks>=(s2_maxmarks)*(33/100) and s3_marks>=(s3_maxmarks)*(33/100):
#         print("Congratulations you Pass the examination")
#     else:
#         print("you are fail because you have less than 33% in one or more of the subjects")
# else:
#     print("you are fail due to total percentage is less than 40")
        
a=input("Enter your comment: ")
spam= False
if ("make a lot of money" in a):
    spam = True
elif ("buy now" in a):
    spam = True
elif ("click this" in a):
    spam = True
elif ("subscribe this" in a):
    spam = True
else:
    spam=False

if spam==True:
    print("This comment is spam")
else:
    print("this comment is not spam")


    



    