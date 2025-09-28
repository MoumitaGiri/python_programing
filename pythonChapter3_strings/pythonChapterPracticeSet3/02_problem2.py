# name = input("Enter your name: ")
# date = input("Enter today's date: ")

# letter = '''Dear {name},\nYou are selected!\n{date}'''
# print(letter.format(name=name, date=date))

# another way to format name and date
letter1 = '''
Dear |<name>|,
You are selected!
|<date>|'''

print(letter1.replace("|<name>|", "Moumita").replace("|<date>|", "14th august 2025"))
