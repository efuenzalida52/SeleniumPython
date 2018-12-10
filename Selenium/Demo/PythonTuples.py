# List [] ordered | indexed | changeable | duplicates
# Tuple () ordered | indexed | unchangeable | duplicates | mutable
# Set {} unordered | unindexed | no duplicates
# Dictionary {K:V} unordered | changeable | indexed | no duplicates

my_tuple = ('Apples', 'Oranges', 'grapes')
print(my_tuple)
print(my_tuple[1])
# using a negitive loops to back
print(my_tuple[-1])
print(my_tuple[0:3])
print(my_tuple[0:2])

for val in my_tuple:
    print(val)

print(len(my_tuple))

my_tuple_2 = ('banana', [1,2,3], ['tokyo','seattle', 'rome'])
print(my_tuple_2)
#tupleception
print(my_tuple_2[2][1])

# while tuples are nto changeable they are muteable/ can be overwritten
my_tuple_2[2][1] = 'New York'
print(my_tuple_2)

print('banana' in my_tuple_2)  # true
print('cherry' in my_tuple_2)  # false
