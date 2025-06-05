# n!=1*2*3*4....*n

def fact(n):
    if n==0 or n==1 :
        return 1
    return n* fact(n-1)
 
print(fact(4))