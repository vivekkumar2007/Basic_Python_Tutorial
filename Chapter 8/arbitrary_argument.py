def add(*numbers) -> int:    # Here add function can take any number of Positional argument as a tuple in numbers
    sum = 0
    for num in numbers:
        sum += num
    return sum
    
print(add(2,6,4,8))   

def multiply(**numbers) -> int :   # Here multiply function can take any number of Keyword-only argumrnt as a dictionary in numbers
    mul = 1
    for num in numbers.values() :
        mul *= num
    return mul
    print(numbers)
print(multiply(a=4, b=3, c=5))   # Here numbers become {'a': 4, 'b': 3, 'c': 5}.