# List [] ordered | indexed | changeable | duplicates
# Tuple () ordered | indexed | unchangeable | duplicates | mutable
# Set {} unordered | unindexed | no duplicates
# Dictionary {K:V} unordered | changeable | indexed | no duplicates

my_set = {'dog', 'cat', 'puppy', 'kitten'}
print(my_set)

for x in my_set:
    print(x)

print('dog' in my_set)

my_set.add('bunny')
print(my_set)

# because it is unordered can add anywhere
my_set.update(['horse', 'fish'])
print(my_set)

len(my_set)

# you HAVE TO specifiy property since it is not ordered
my_set.remove('fish')
print(my_set)
my_set.discard('horse')
print(my_set)
# difference between remove & discard
# if an item has been removed it will throw an error if u try 2 remove again
# if item have been discarded it will NOT throw an error if u try 2remove again
# my_set.remove('fish')
# my_set.discard('horse')


my_set.pop()
my_set.clear()
print(my_set)

del my_set

# sets can contain different data types and objects
my_set_2 = {'Apples', 1, 7, (3, 4, 5)}
print(my_set_2)

my_list = ['!', '@', '#']
print(my_list)
my_set_3 = set(my_list)
print(my_set_3)

# UNION | INTERSECTION | DIFF | SYMMETRIC DIFF
A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}
print(A.union(B))
# | is symbol for a union
print(A | B)
#  & is  symbol for an intersection
print(A.intersection(B))
print(A & B)
# - is the symbol for difference
print(A.difference(B))
print(A - B)
print(B - A)
# ^ is the symbol for symmetric difference
# prints the elements that are the same between sets
print(A.symmetric_difference(B))
print(A ^ B)
#
