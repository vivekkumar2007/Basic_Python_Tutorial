for i in range(1,11):
    for j in range(1,11):
        print(i*j, end='\t')
    print()
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
sum=0
for row in matrix:
    s=0
    for element in row:
        s+=element
    sum +=s
print(sum)

for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Your code here
transpose = []
for i in range(len(matrix[0])):
    rows=[]
    for j in range(len(matrix)):
        rows.append(matrix[j][i])
    transpose.append(rows)
for i in transpose :
    print(i)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

falatten_matrix=[]
for i in matrix :
    for j in i:
        falatten_matrix.append(j)

print(falatten_matrix)

grid = [ ['a', 'b', 'c'], ['d', 'e', 'a'], ['f', 'a', 'h']]
Target='a'
count=0
for row in grid:
    for element in row:
        if element==Target :
            count +=1
print(count)

pascle_triangle=[[1]]
for i in range(1,6):
    row =[1]*(i+1)
    for j in range(1,i):
        row[j]= pascle_triangle[i-1][j-1] + pascle_triangle[i-1][j]
    pascle_triangle.append(row)

for row in pascle_triangle:
    print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum = 0
for i in range(len(matrix)):
    j = len(matrix[0]) - 1 - i  # Calculate j based on i
    sum += matrix[i][j]

print(sum)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
numbers_set=set(numbers)
frequency_list=[]
for unique_value in numbers_set :
    count=0
    for num in numbers:
        if unique_value==num :
            count+= 1
    frequency_list.append([unique_value,count])

print(frequency_list)

for i in range(1,6):
    for j in range(6-i):
        print('*',end='')
    print()

strings = ["level", "world", "radar", "hello", "civic"]
palindrome=[]
for string in strings:
    if string==string[::-1]:
        palindrome.append(string)
    else:
        pass
print(palindrome)
        
three_d_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
flatten_list=[]
for i in three_d_list:
    for j in i:
        for k in j:
            flatten_list.append(k)

print(flatten_list)

list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7, 8]
common_list=[]
for i in range(len(list1)) :
    for j in range(len(list2)):
        if list1[i]==list2[j] :
            common_list.append(list1[i])
print(common_list)

matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
Sum=[]
for row in matrix:
    s=0
    for i in range(len(row)):
        s+=row[i]
    Sum.append([row,s])
print(Sum)
numbers = [1, 2, 3, 4, 5, 6, 7] 
target_sum = 8
pairs=[]
for i in numbers:
    for j in numbers:
        if i+j==target_sum:
            pairs.append([i,j])
print(pairs)

for i in pairs:
    for j in pairs:
        if i !=j:
            if i[0]==j[1] and i[1]==j[0]:
                pairs.remove(j)
print(pairs)






