import numpy as np
arr = np.array([[6,5,3],
                [7,1,9],
                [8,3,0]])

print(arr.argmin())    # return index of lowest element
print(arr.argmax())    # return index of highest element
print(arr.argsort())

print(arr.max())
print(arr.min(axis=0))
print(arr.max(axis=1))

