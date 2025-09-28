inp = "interview"
count = 0
vowel = "aeiou"

for ch in inp:
    print(ch)
    if(ch in vowel):
        count = count + 1
print(count)