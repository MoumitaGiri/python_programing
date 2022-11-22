
lst1 = [i for i in input().split()]
lst2 = [x for x in input().split()]

lst1, lst2 = lst2, lst1
print(lst1,lst2)

lst1 = [y for y in input().split()]
lst1[0], lst1[-1] = lst1[-1], lst1[0]
print(lst1)

lst2 = [str(y) for y in input().split()]
lst2[0], lst2[-1] = lst2[-1], lst2[0]
print(lst2)

