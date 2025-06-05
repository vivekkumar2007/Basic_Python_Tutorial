# sort the character in a string
mystr = "Hello , Vivek"
# char = "abcdefghijklmnopqrstuvwxyz"
# sorted_str = []
# for i in char:
#     sorted_str.extend([c for c in mystr.lower() if c==i])

# sorted_str= "".join(sorted_str)
# print(sorted_str)


# mystrlst=[char for char in mystr.lower() if char.isalpha()]
# mystrlst.sort()
# sorted_str = "".join(mystrlst)
# print(sorted_str)

# lst =[]
# for i in mystr:
#     if i.isalpha():
#         lst.append(i)
# string = "".join(lst)
# print(string)
# mystr = [c for c in mystr if (c.isalpha() or c.isspace())]
# mystr = ''.join(mystr)
mystrs = mystr.split()
print(len(mystrs))