# Write a python program using function to convert celsius to fahrenheit

'''
formula:
c/5 = (f-32)/9
c = 5 * (f-32)/9
'''

def cel_fah(f):
    c = 5 * (f-32)/9
    return c

f = int(input("enter the temperature: "))    
print(f"Convert: {cel_fah(f)} C")

print(round(cel_fah(f))) # round function is used to make the output figure round of

