# Difference between NumPy array and List in Python

# array can store only one types of Data types but list can store more than one types of data types
# Numpy array required importing a module but list doesn't
# NumPy array do fast work than List
# Modification capibility is high in List than Numpy array.
# NumPy array is Convenient to use.

import numpy as np
x = [1,2,3,4]
y = np.array(x)
print(y)
print(type(y))   
print(y.ndim)

ar2 = np.array([[1,2,3,4],[2,3,6,7]])
print(ar2)
print(ar2.ndim)

ar3 = np.array([1,2,3,4],ndmin = 10)
print(ar3)
print(ar3.ndim)

# l= []
# for i in range(1,5):
#     int_1 = int(input("enter : "))
#     l.append(int_1)

# print(np.array(l))



