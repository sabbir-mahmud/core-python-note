# list and matrix
# list/Array in python
# list
subject = ['c', 'c++', 'Java', 'Python']
print(subject)
print(subject[0])
print(subject[3])

subject.append('JavaScript')
# Append add an item in end of the list
print(subject)

subject.sort() 
# Sorts the items
print(subject)

subject.reverse() 
# Reverses the order of the list
print(subject)

subject.remove('c') 
# Removes the first item with the specified value
print(subject)

subject.pop(2)
# Removes the element at the specified position 
print(subject)

subject.insert(2, 'Dom')
#Adds an element at the specified position 
print(subject)

x = subject.index('c++')
# Returns the index of the first element with the specified value 
print(x)

y = subject.count('Python')
# Returns the number of elements with the specified value
print(y)

# Matrix 
# Matrix means two or more list in one list
subject = [
    ['A', 'B','C'],
    ['B', 'C', 'D']
]

print(subject)
subject[0][2] = 'F'
print(subject[0][2])

for row in subject:
    for col in row:
        print(col)
