# print even numbers between 2 - 20

a =2
b = 20

for i in range(2, 21):
    if i % 2 == 0:
        print(i)
    i += 2
        
count = 2    
while count < 21:
    if count % 2 == 0:
        print(count)
    count += 2