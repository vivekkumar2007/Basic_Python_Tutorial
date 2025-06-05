import numpy as np
random_integer_data = np.random.randint(4000, size = 4000)
# def Fsum(n):
#     S = 0
#     for i in range(n):
#         S += random_integer_data[i]
#     return S

# def Lsum(n):
#     s=0
#     for i in range(n):
#         s += random_integer_data[4000-i-1]
#     return s

# print("Sum of First 100 number is =",Fsum(100))
# print("Sum of Last 100 number is =",Lsum(100))
# print("Sum of First 2000 number is =",Fsum(2000))
# print("Sum of Last 2000 number is =",Lsum(2000))

def SumAndMean():
    Lst = []
    for i in range(1, int(4000/100)+1):
        Lst.append(i)
    print(Lst)

SumAndMean()

