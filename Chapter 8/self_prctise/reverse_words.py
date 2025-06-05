def reverse_strings(str):
    words = str.split()
    reverse_word=words[::-1]
    
    reverse_word = ' '.join(reverse_word)
    return reverse_word

myString = input("Enter the string: ")
result = reverse_strings(myString)
print(result)
