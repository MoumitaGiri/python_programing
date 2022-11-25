# find max number in given list
l = [int(x) for x in input().split(' ')]
list = max(l)
print(list)

# find min number in given list
l = [i for i in input().split(' ')]
list1 = min(l)
print(list1)

# sort the given list
l1 = [int(x) for x in input().split(' ')]
l1.sort()
print(l1)

# reverse the given list
l2 = [int(y) for y in input().split(' ')]
l2.reverse()
print(l2)

# reverse in ascending order 
l3 = [int(e) for e in input().split(' ')]
l3.sort(reverse = True)
print(l3)

# way to find whether given number exist in list or not
l = [int(x) for x in input().split(' ')]
i = int(input("enter a number")) 
x = 0
for x in l:
  if i in l:
    print("exist")
  else:
    print("not exist")

    '''
    note: doubt is when we add for loop here it gives 4 time exist means 4 times execute but if I removed for loop then execute 1 time and gives proper result
    for x in l: 
    '''
#count the odd number and even number in list 
l = [int(i) for i in input().split(' ')]
odd_num = [int(num) for num in l if num % 2 == 1]
odd_count = (len(odd_num))
print("even number count:", len(l) - len(odd_num))
print("odd number count:", odd_count)

'''
note: doubt is why this error and is it required to store the length of odd_num in another variable why cant we pass in same line 
len(l) - len(odd_num))
'''
#count the odd number and even number in list 
l = [int(i) for i in input().split(' ')]
odd_num = [int(num) for num in l if num % 2 == 1]
odd_count = (len(odd_num))
print("even number count:", len(l) - odd_count)
print("odd number count:", odd_count)

#count the positive number and negative number in list 
l = [int(x) for x in input().split(' ')]
pos_num = [int(num) for num in l if num >= 0]
positive = (len(pos_num))
print("negative number count:", len(l) - positive)
print("postive number count:", positive)

'''
occurance program
'''
l = [int(t) for t in input().split(' ')]  #take list of element with user input
d= dict() #declare empty dictionary
for i in l: #check if value of i in list l
  if i not in d: # check if value of i is not in dictionary
    d[i]=1 #if true then store the value 
  else:
    d[i]=d[i]+1  # if false then else part execute

print(d)

#print postive and negative number
list = [int(num) for num in input().split(' ')]

'''
wrong output coming error 
'''

for i in list:
  if (num >=0):
    d[i]=1
    print("positive",num)
  else:
    print("negative", list - num )

#list = [int(x) for x in input().split(' ')]
'''
Note : why i got this error ?? 'ValueError: invalid literal for int() with base 10:' when given user input
'''
#print postive number
list = [3, 5 , 6 , -9 ,-8, -7]
for i in list:
  if (i >=0):
    print(i)
  else:
    print("negative")

#sort the list then print the negative number from list
list = [int(x) for x in input().split(' ')]
#list = [3, 5, 6, 7, 8, -9, -7, 0, -4, -5, -6, -3, -2, 9]
#list.sort(reverse = True)
list.sort()
print(list)
for i in list:
  if (i<=0):
    print([i])
  else:
    print("postive")

#print even number from list
list = [int(x) for x in input().split(' ')]
for i in list:
  if (i%2==0):
    print(i)
  else:
    print("odd")

#print odd numnber  from list 
list = [int(x) for x in input().split(' ')]
for i in list:
  if (i%2 == 1):
    print(i)
  else:
    print("even")




