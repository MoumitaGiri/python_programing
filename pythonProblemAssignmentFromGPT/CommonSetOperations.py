# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a.union(b))        # {1, 2, 3, 4, 5, 6}
# print(a.intersection(b)) # {3, 4}
# print(a.difference(b))   # {1, 2}


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}
# print(set1.intersection(set2)) # {4, 5}
# print(set1.difference(set2)) # {1, 2 , 3}

a = {1, 3}
b = {2, 4}
print(b.difference(a)) # {2,4}
print(a.difference(b)) # {1,3}
print(b.union(a)) #{2, 4, 1, 3} / {1, 2, 3, 4} unordered
print(b.intersection(a)) # {set()} no intersection point / common point
b.add(2)
print(b)