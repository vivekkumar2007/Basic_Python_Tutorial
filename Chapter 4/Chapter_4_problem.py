#1
# f1=input("Enter first frute name: ")
# f2=input("Enter second frute name: ") 
# f3=input("Enter third frute name: ")
# f4=input("Enter fourth frute name: ")
# f5=input("Enter fifth frute name: ")
# f6=input("Enter sixth frute name: ")
# f7=input("Enter seventh frute name: ")

# l1=[f1,f2,f3,f4,f5,f6,f7,]
# print("Your list of Fruits:",l1)

#2
a=[3,5,6,3,44]
print(a[0]+a[1]+a[2]+a[3]+a[4])
print(sum(a))

import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Click me", command=lambda: print("Button clicked"))
button.pack()
root.mainloop()
