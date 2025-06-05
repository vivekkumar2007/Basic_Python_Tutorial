def checkVowels(n):
    match n:
        case 'a': return "Vowel alphabet"
        case 'e': return "Vowel alphabet"
        case 'i': return "Vowel alphabet"
        case 'o': return "Vowel alphabet"
        case 'u': return "Vowel alphabet"
        case _ : return "simple alphabet"
n=input("Enter a alphabet:")
n1=n.lower()
print(checkVowels(n1))