# if else
# if 5 > 3:
#     print('5 is greater than 3')
#
# num = 0  #-1
#
# if num > 0:
#     print ('this is a positive number')
#
# elif num == 0:  # else if statement
#     print('awesome!')
#
# else:
#     print('this is a negitive number')


# Loops
# 4 loops
numList = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for val in numList:  # as long as there are values print something
    sum = sum + val
    print('There are', sum, 'Anakins')

foodList = ['pizza', 'cookies', 'ice cream', 'sandwhiches', 'fruits', 'veggies', 'spahgetti', 'dirt']
for val in foodList:
    print(val)
else:
    print('No foods for you')

# while loop
print('Enter a number:')
num = int(input())
sum = 0
i = 1

while i < num:
    sum = sum + i
    i = i+1
print("Total is :", sum)
