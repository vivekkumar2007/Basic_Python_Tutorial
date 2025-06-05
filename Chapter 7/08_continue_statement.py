for i in range(10):
    if i==5 :  
        continue    #when i = 5 iteration is not done that is it not print 5
    print(i)
print("Done")

# example usage; we have to print only even number till 20 then
for i in range (21):
    if i%2 == 1 :
        continue
    print(i)