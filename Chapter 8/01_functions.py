def percent(marks)  -> float:
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

marks1 = [43,53,54,87]
percentage1=percent(marks1)

marks2= [65,78,98,65]
percentage2=percent(marks2)
print(percentage1, percentage2)