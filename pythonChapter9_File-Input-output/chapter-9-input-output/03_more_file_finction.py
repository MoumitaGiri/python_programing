f = open("file.txt",)

lines = f.readlines() # readlines() function is used to read more lines # readlines() --> <class 'list'>

print(lines, type(lines)) # to check type of 

f.close()