#Encapsulation = Abstraction + data hidining, 
#Abstraction=> Showing essential features and hiding non-essential features

# private method and variable, defined by __(underscore 2 times)
# To use private method, _classname__methodname

class Account():
    def __init__(self) -> None:
        self.__balance = 0
    
    def setBalance(self, balance):
        self.__balance = balance

    def __setBalancePrivate(self, balance):
        self.__balance = balance
    
    def getBalance(self):
        return self.__balance
    

obj = Account()
print(obj.getBalance())
obj.setBalance(20)
print(obj.getBalance())
obj._Account__setBalancePrivate(30)
print(obj.getBalance())

obj.__balance = 50 # will not work seems private
print(obj.getBalance())
