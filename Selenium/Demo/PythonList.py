# List [] ordered | indexed | changeable | duplicates
# Tuple () ordered | indexed | unchangeable | duplicates
# Set {} unordered | unindexed | no duplicates
# Dictionary {K:V} unordered | changeable | indexed | no duplicates

my_list = ["Tokyo", "Rome", "Santiago"]
print(my_list)
print(my_list[2])

# changes index given to new value
my_list[1] = "New York"
print(my_list)

#using a loop
for val in my_list:
    print(val)

print(len(my_list))

# using .
my_list.append("Rome")
print(my_list)
my_list.insert(4, 'Seattle')
print(my_list)
my_list.remove('New York')
print(my_list)
# pop w/ no argument follows LIFO/ pops last element
my_list.pop()
print(my_list)
my_list.insert(4, 'Seattle')
print(my_list)
my_list.pop(3)
print(my_list)

del my_list[2]
print(my_list)

my_list.clear()
print(my_list)

fruit_list = ['apples', 'pears', 'grapes', 'oranges']
print(fruit_list)
# reverses list order printed
fruit_list.reverse()
print(fruit_list)

my_list_2 = ["apples", 1, 2, 3.0]
# listception / nested list
my_list_3 = ["apples", [1, 2, 3], ['a', 'b', 'c']]
print(my_list_3[1][1])
