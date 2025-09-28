# Create a list of vowels from a word.

inp = "moumita"
# out = ['o', 'u', 'i', 'a']
vowel = "aeiou"
list = []
# list.append(inp)
# print(list)
for character in inp:
    if(character in vowel):
        list.append(character)
print(list)
