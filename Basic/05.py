# Python Operators
# Arithmetic operators
from math import * 

num1 = 18
num2 = 2

sum = num1 + num2
sub = num1 - num2
times = num1 * num2
div = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2
floor = num2 // num2

print(sum)
print(sub)
print(times)
print(div)
print(modulus)
print(exponentiation)
print(floor)

# Assignment Operators

a = 10
b = 20

a = a+b   #  = Operators
print(a)

a += 10   #  += Operators
print(a)

a -= 10   #  -= Operators
print(a)

a *= 10   #  *= Operators
print(a)

a /= 10   #  /= Operators
print(a)

a %= 10   #  %= Operators
print(a)

a **= 10   #  **= Operators
print(a)

a //= 10   #  //= Operators
print(a)


# Comparison Operators

x = 5
y = 5

print(x == y)     #  == Operators
print(x != y)     #  != Operators
print(x > y)      #  > Operators
print(x < y)      #  < Operators
print(x >= y)     #  >= Operators
print(x <= y)     #  <= Operators

# Logical Operators

c = 10
d = 10
e = 10

if (c == 10 and d == 5):    # and operator
    print('Condition Match')

else:
    print('Not Match')


if ( c == 10 or d == 5):    # or operator
    print('One Match found')

else:
    print('Not Match') 


if not ( c == 10):    # not operator
    print('One Match found')

else:
    print('Not Match') 

#ternary Operator
num4 = 57
num5 = 37

print(num4 if num4 > num5 else num5)

