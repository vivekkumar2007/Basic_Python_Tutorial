x=input("Enter First Number: ")
y=input("Enter Second Number: ")
x=int(x)
y=int(y)
'''if x<50: 
    #inner if-else structure is only evaluated if ‘x’ is less than 50.
    if y<50: 
        print("Both x and y is less than 50")
    else :
        print("x is less than 50, but y is not")
else :
    print("Both x and y is not less than 50")'''

if x<50 and y<50 :
    print("Both x and y is less than 50")
elif x<50 and y>50:
    print("x is less than 50, but y is greater than 50")
elif x>50 and y <50 :
    print("x is greater than 50 but y is less than 50")
else :
    print("Both x and y is greater than 50")