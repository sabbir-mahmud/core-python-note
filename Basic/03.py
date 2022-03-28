# Dictionaries and tuples and set

# Dictionaries
subject = {
    'name' : 'Sabbir Mahmud',
    'age' : 23,
    'Address' : 'Ullapara, Sirajganj'
}

users = {
    1 : 'Sabbir',
    2 : 'Aria',
    3 : 'Jasof'
}

print(subject)
print(subject['name'])
print(subject.get('age'))
print(users)
print(users[1])

# Tuples
student = (
    'Sabbir Mahmud',
    'Anisul Islam',
    'Kamrul Hassan'
)

print(student)
print(student[1])

# Set
num = { 1,2,3,4,5,5,6}
print(num)

number = set([1,2,3,3,4,5,6])
print(number)

number.add(19)
print(number)

number.remove(2)
print(number)

print(num.union(number))
print(num & number)
print(num - number)