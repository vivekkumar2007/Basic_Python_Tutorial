greeting="Good morning, "
name="Vivek kumar."
#string concatenation
c=greeting +name
print(c)

#string slicing
name="Vivek"
print(name[0:4])  #this print first four alphabet of string 'name' i.e upto index 0 to 3
print(name[:4])   #this is same as name[0:4]
print(name[1:])   #this print index 1 to last index

#negative slicing
print(name[-4:-2]) # the last alphabet is -1 index and 2nd last index is given to -2 index and so on. as here -4 index is 'i' and -2 is index is 'e' so it print'ive'

#skipping alphabet

greeting="GoodMorning"
print(greeting[1:7:2]) # i.e it skip one alphbet from 1 index to 3 index and 3 to 5 index
print(greeting[1:7:3])