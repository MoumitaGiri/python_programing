f = open("file.txt")
data = f.read()
print(data)
f.close # mandatory to write this line while reading a file

# 'with' statement

# with in as f:
#     f.read()