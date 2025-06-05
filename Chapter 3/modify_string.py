s1 = "WORD"
print("Original String :", s1)

l1 = list(s1)
print(l1)

l1.insert(3,"L")

s1 = "".join(l1)
print("Modified String :", s1)