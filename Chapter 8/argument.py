def func(name, age):
    print(f"Your name is {name} and your age is {age}.")

func(name = "Vivek Kumar", age = 17)    # This is a keyword argument
func("Satyam", 19)                      # This is positional argument
func("Avanish Kumar", age = 20)         # This is mixed positional + keyword argument. but possitional argument to be write first
# func(name = "Nirbhik Viswas", 19)     # This gives an Error


""" Generally In Function It is not fixed i.e it can take both positional or Keyword argument, 
    but We can fix only Keyword argument or Positional Argument"""

def add(a: int, *,b: int) ->int :
    return a+b 

print(add(2, b = 5))    # here b is an Keyword-only Argument
# print(add(2,5))    # If we do this then we will get an error


def multiply(a,b,c,/, d) -> int:
    return a*b*c*d 

print(multiply(1,2,3,4)) # Here a,b,c is a Positional-only argument 