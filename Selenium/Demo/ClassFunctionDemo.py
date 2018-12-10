# self is a variable in python, used as very first parameter/argument for EVERY function.
# You can name it anything


class FirstClass:

    name = 'Elizabeth'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a+b)

# because we are passing new arguments into FirstClass object, default values are overwritten

x = FirstClass('Anakin', 1)
print(x.name)
x.sum(10, 10)
# deletes object reference OR particular property reference. Placing is important!!
# where del x.name is currently will still show  Anakin b/c name was printed b4 property was deleted.
# calling name again would print default 'Elizabeth'
del x.name
print(x.age)
# print(x.name)


