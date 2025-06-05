# creating an empty set
a=set()
print(type(a))

#adding values to an empty set
a.add(4)
a.add(4)   # adding a value repetedly doesn't changes the set
a.add(5)
a.add(8)
# a.add([4,5,3])  # it gives error because list and dict is unhashable i.e it is changeable
a.add((4,5,6))    # it  doesn't give error because tuple ishashable i.e it is not changeable
print(a)

print(len(a))  # print the length of set a
a.remove(4)    # remove 4 from the set a
print(a)

print(a.pop())  # remove an arbitrary element from the set and return the element removed
print(a)

x= set([2,5,3,7,4,3,5])
print("x= ", x)

y = set([6,1,3,2,9,8])
print("y =", y)

# Union and Intersection of Two sets
intersec= x.intersection(y)
print(x&y)  # This is also x intersection y
print(intersec)

union = x.union(y)
print(x|y)  # this is also x intersection y
print(union)

print(x^y)