class Dog:
    def __init__(self, name):
        self.name = name
        print("Object with name: {} creates".format(name))
    
    def talk(self):
        print("voice woof")
        
    def printName(self):
        print("Name is: {}".format(self.name))
        
    def __str__(self) -> str:
        return self.name

charlie = Dog("charlie")
charlie.talk()
charlie.printName()

bhuro = Dog("bhuro")
bhuro.talk()
bhuro.printName()

print(charlie)