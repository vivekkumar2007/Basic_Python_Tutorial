f = open("sample.txt", "w")   # sample.txt file is not created by me, but we open it wit "a" or "w" mode then python creates this file
f.write("Hi, How are you. Hope you are doing well.")
f.write("\nI am writing another line in sample.txt file") # If we open file in "w" mode then it completely overwrite data i.e it erase all data that it already have
f.close()