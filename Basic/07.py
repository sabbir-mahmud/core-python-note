# While loop

i = 1

while i <=5:
    print(i)
    i = i + 1
print('While Loop End')

# for loop

sum = [0,1,2,3,4,5,6]

for i in sum:
    print(i)
    print('For loop end')


# Break And Continue
# Break

i = 1

while i <=5:
    print(i)
    i = i + 1
    if i == 3:
        break
    
print('Break End')


# Break And Continue
# Continue

i = 1

for i in 'Sabbir':
    if i == 'b':
        continue
    print(i)

print('Continue End')