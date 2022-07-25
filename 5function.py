# user defined funtion
# Built-in function
    # abs(): return absoulute value
    # all(): return all items an iterable object are true
    # any(): return True if any item in an iterable object is true
    # ascii(): return a readable version of an object and replaces non-anscii chars with an 'escape' char
    # bin(): return binrary version of object
    # bool(): retur boolean value of a specific object
# Lambda function
    #its anonymous single line function, no name, can not contain more than one experssion    

def function_name(arg1, arg2):
    # calculation
    return arg1+arg2

#print(function_name(1,2))


# Lambda function
l = lambda x,y:x+y
print(l(2,4))

# power of lamba, can put inside another function
def myFunc(n):
    return lambda a : a + n

mySum = myFunc(3)
print(mySum(10))