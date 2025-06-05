string=input("Enter a string\n")
vowels = "aeiou"
count = 0
for char in string.lower():
    if char in vowels:
        count +=1
print("No. of Vowel in the given string is =",count)

