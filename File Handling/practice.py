# """ Q. Create a new file "practice.txt" using python. Add the following data in it :
#         Hi everyone
#         We are learning File I/O
#         using Java.
#         I like programming in Java.
        
#       WAF that replace all occurences of "Java" with Python in above file."""

# with open("practice.txt","w") as f:
#     f.write("""Hi everyone
# We are learning File I/O
# using Java.
# I like programming in Java.""")
    
# with open("practice.txt","r") as j:
#     data = j.read()
#     data = data.replace("Java","Python")

# with open("practice.txt", "w") as f:
#     f.write(data)
#     if "learning" in data:
#         print("Yes")
#     else:
#         print("No")

""" Q. WAF to find in which line of the file does the word "learning"
       occur first. 
       Print -1 if word not found
       
       From a file containing numbers separated by comma, print the count of even numbers."""

# def check_for_line():
#     data = True
#     line = 1 
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if "learning" in data:
#                 return line
            
#             line+=1
#     return -1
# print(check_for_line())


# with open("number.txt","w") as f:
#         f.write("2,53,2,69,54,12,33")


def check_even():
    with open("number.txt","r") as f:
        data = f.read()
        # num=''
        # lst = []
        # for i in range(len(data)):
        #     if data[i]!=",":
        #         num += data[i]
        #         if i==len(data)-1:
        #             lst.append(int(num))
        #     else:
        #         lst.append(int(num))
        #         num = ''

        lst1 = data.split(",")
        count = 0
        print(lst1)
        for n in lst1:
            if int(n)%2 ==0:
                count +=1
        

    return count

print(check_even())