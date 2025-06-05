         #keys       #value
myDict = {"Fast":"In a quick manner" , 
          "Vivek":"A Coder",
          "marks":"[2,4,54,6]",
          "anotherdict":{'vivek':'player'},
          1:2
          }
# Dictionary method
print(list(myDict.keys()))  #print the keys of the dictionary
print((myDict.values()))    #print the values of the dictionary
print((myDict.items()))     #print the (key,value) for all contents of the dictionary
print(myDict)
updateDict={
    "Satyam":"Friend",
    "avanish":"Friend"
}
myDict.update(updateDict) #updates the dictionary by adding the keys value pairs from updateDict
print(myDict)

print(myDict.get("Vivek")) 
print(myDict["Vivek"])

print(myDict.get("Vivek2")) # this gives none beacause in myDict 'Vivek2' is not present
#print(myDict["Vivek2"])  # This gives errror because in myDict 'Vivek2' is not present
