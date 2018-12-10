# def keyword defines function
# def function_name(parameter):
# body


def printfunction():
    print('Hello!')


# function(parameter = 'thing')
def greetingfunction(name):
    print("Hi "+name)


# greetingFunction()
greetingfunction('Elizabeth')


def sum(a, b, c):
    print(a+b+c)


sum(5, 5, 5)


def returnit(a, b):
    """This is a description of this function. three quotes to create """
    return (a+b)


x = returnit(7, 7)
print(x)
