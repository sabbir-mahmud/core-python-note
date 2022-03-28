# function and lambda function
# function
def sum(x, y):
    print(x+y)

sum(12,25)

# return value from function

def large (a, b):
    if a > b:
        return a
    else:
        return b

print(large(100,110))

# store function in a variable
maximum = large
print(maximum(10,15))

# xxargs work like tuples
def student(*details):
    for x in details:
        print(x)


student(101, 'Anisul Islam')

# xxxargs work like dictionaries
def number(**number):
    print(number)
    print(number['num1'])

number(num1= 102, num2= 301)

# lambda function
print((lambda a , b : a + b )(2 , 5))

sum = ( lambda a , b : a-b ) (7 , 5)
print(sum)