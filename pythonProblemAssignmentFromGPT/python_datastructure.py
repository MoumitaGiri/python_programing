#list
lst = [2, 4, 6, 9, 5]
lst.append(70)       #add
lst.remove(9)        #remove
lst[4] = 130         #update
lst.reverse()        #reverse
lst.sort()           #sort
lst.insert(4, 200)   #insert
print(lst)           #print

#tuple
tpl = (1, 7 ,8, 30, 12, 8, 90, 5, 14, 8)
tpl.count(8)
tpl.index(12)
#tpl[0] = 100   #cannot update value its immutable

#set
st ={3, 86, 35, 86, 14}
st.remove(86)
st.add(20)

#dictionary
dct = {
    "name": "Moumita",
    "age" : 26,
    "city": "Bangalore",
    "favorite_food": "Pantabhaat"
}
dct["location"] = "whitefield" #add
dct["age"] = 30                #update
dct.pop("city")                #remove
print(dct.keys())              #print keys
print(dct.values())            #print values

print(f"list with at least 2 operations: {lst}, tuple with at least 2 operations: {tpl}, set with at least 2 operations: {st}, dictionary with at least 2 operations: {dct}")
