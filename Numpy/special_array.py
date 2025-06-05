import numpy as np
ar_zero = np.zeros(4)
ar_zero1 = np.zeros((3,4))
print(ar_zero)
print()
print(ar_zero1)

ar_one = np.ones(4)
print(ar_one)

# Empty array
ar_empty = np.empty(4)
print(ar_empty)

# Range
array = np.arange(1,9,0.5)
print(array)

# Diagonal
ar_dia = np.eye(3)
ar_dia1 = np.eye(3,5)
print(ar_dia)
print(ar_dia1)

# linspace               
ar_lin = np.linspace(2,10,5)    # 2 se 10 ke bich me 5 numbers create honge
print(ar_lin)

