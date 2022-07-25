from ast import arg


class Person:
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        print('My name is {}'.format(self.name))
        
class Engineer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "Engineer"
    
    def sayProfession(self):
        print("My profession is {}".format(self.profession))
        
class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "Doctor"
    
    def sayProfession(self):
        print("My profession is {}".format(self.profession))

        
engineer = Engineer("Vipul")
engineer.getName()
engineer.sayProfession()

doctor = Doctor("Dilip")
doctor.getName()
doctor.sayProfession()

# How to avoid Overriding by multiple args with smartly 
def add(*args):
    if(len(args) == 2): return args[0] + args[1]
    result = 0
    for x in args:
        result += x
    return result

print(add(2,3)) 
print(add(2,3,4)) 
print(add(2,3,4,5)) 