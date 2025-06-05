# file = open(r"C:\Users\vivek\Downloads\_Getintopc.com_DS.SolidWorks.2021.SP0.0.Premium\DS.SolidWorks.2021.SP0.0.Premium\_SolidSQUAD_\readme.txt","r")
# f = open(r"C:\Users\vivek\OneDrive\Attachments\Python Tutorial\File Handling\demo.txt","r")
# line1 = f.readline()     # It reads one line at a time
# data = f.read()      # if some data get read already then only left data is readed.

# print(line1)
# print(data)  
# print(type(line1))
# f.close()

""" BY WITH SYNTAX """

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
with open("demo.txt","w") as f:
    f.write("new data")