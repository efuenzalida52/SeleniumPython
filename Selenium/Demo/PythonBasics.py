# highlight & ctrl + forward slash [/] to comment/uncomment single & multiple lines
print("Hello World...")

# variable ARE case sensitive
# letters, underscore, numbers
x = 5
y = 'Automation'

print(x)
print(y)

print('Hello this is an ' + y)

# can changes value sof existing variables
x = 10
y = 20
print(x+y)

# 4 space or tab
text = '10 is greater than 5'
if 10 > 5:
    print(text)

# creating functions
def sum(a,b):
    print(a+b)
test = sum(20, 30)

# python auto converts number types, but you can check the type like so...
j = 5
k = 2.7
x = 6j

print(type(j))
print(type(k))
print(type(x))

# casting
x = int(2)  # 2 b/c you indicated int
y = int(2.5)  # 2 b/c you indicate int
z = float(1)  # 1.0 b/c you indicated float
s = str(10)  # stored as '10' b/c you incidate it is string- so somethign liek x+s will result in error

print(x, y, z, s)

# casting strings
x = "ABCDEFG hijklmnop"
print(x[1])  # grabs 2nd character in string/ 2nd number in index (index starts at 0)
print(x[6:11])  # prints characters  7-11
print(len(x))  # prints length of entire string variable
print(x.lower())  # makes variable all lowercase
print(x.upper())  # makes variable all uppercase
y = '   why u extra spaces?  '

print(y)
print(y.strip())  # removes any extra spaces at beginning/end of variable
print(y.replace('u', 'I'))  # finds and replaces characters
print(y.split('u'))  # splits variable string into more than one,
# BECAREFUL variable teh split in on no longer appears


# input

print('Please enter your name:')
name = input()
print('Hello ' + name)

