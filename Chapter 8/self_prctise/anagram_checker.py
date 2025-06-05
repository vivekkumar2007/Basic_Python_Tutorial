# my code
s1 = input("Enter the first string\n") 
s2 = input("Enter the second string\n") 
is_anagram = False
for char1 in s1 :
    for char2 in s2 :
        if char1 in s2 and char2 in s1 :
            is_anagram =True

if is_anagram :
    print("given strings are anagram to each other")
else:
    print("given string are not anagram to each other")

# ai code
# Take input from the user
s1 = input("Enter the first string:\n").replace(" ", "").lower()
s2 = input("Enter the second string:\n").replace(" ", "").lower()

# Check if sorted versions of the strings are equal
if sorted(s1) == sorted(s2):
    print("Given strings are anagram to each other")
else:
    print("Given strings are not anagram to each other")
