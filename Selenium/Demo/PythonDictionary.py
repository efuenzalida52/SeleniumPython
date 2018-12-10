# List [] ordered | indexed | changeable | duplicates
# Tuple () ordered | indexed | unchangeable | duplicates
# Set {} unordered | unindexed | no duplicates
# Dictionary {K:V} unordered | changeable | indexed | no duplicates

my_dictionary = {
    'category': 'person',
    'name': 'Collin',
    'occupation': 'student',
    'age': 30
}

print(my_dictionary)
print(my_dictionary['name'])
# What is the point of using get over above?
print(my_dictionary.get('occupation'))
# following print makes a line break in terminal output

print('\n')
print(my_dictionary.values())
print('\n')

# loops w/ dictionaries
for x in my_dictionary:
    print(my_dictionary[x])
print('\n')

for x in my_dictionary:
    print(x)
print('\n')

for x, y in my_dictionary.items():
    print(x, y)
print('\n')

my_dictionary['name'] = 'Jack'
print(my_dictionary)
print('\n')

my_dictionary['Fav Color'] = 'Red'
print(my_dictionary)
my_dictionary['Least Color'] = 'Pink'
print(my_dictionary)
print('\n')

my_dictionary.pop('Fav Color')
print(my_dictionary)
my_dictionary.popitem()
print(my_dictionary)
print('\n')

del my_dictionary["occupation"]
print(my_dictionary)
print('\n')

my_dictionary.clear()
print(my_dictionary)

del my_dictionary


