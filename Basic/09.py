# object orented programming
# class
class User:
    # class attribute
    user = 'Pro-Net User'

    # instance attribute
    def __init__(self,name,mail):  # build in special method
        self.name = name
        self.mail = mail

# instance
u1 = User('Anisul Islam', 'anis@gmail.com')

# instance method
class Se:
    # class attribute
    employee = 'Software engineer'

    # instance attribute
    def __init__(self,name,mail):  # build in special method
        self.name = name
        self.mail = mail

    def __str__(self):  # build in special dunder method
        return (f"Employee Type: {self.employee} ,\n name: {self.name} ,\n mail: {self.mail}")

    def printit(self): 
        print(self.name) # instance method

# instance 
se1 = Se('Sabbir Mahmud' , 'Sabbir@gmail.com')
print(se1)
se1.printit()