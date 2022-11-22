list = ["a", "b","c","d"]
'''
list.insert(2, "e")
print(list)


mylist = [1, 79, 56, 54]
mylist.insert(3, 89)
print(mylist)


arr1 = [3, 4, 6, 7, 9]
arr2 = [1, 2, 5, 8, 0]

arr1.extend(arr2)
print(arr1)
'''

arr3 = [i for i in input().split(' ')]
arr4 = [x for x in input().split(' ')]
arr3.extend(arr4)
print(arr3)



