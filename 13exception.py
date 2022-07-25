#Exception: run time error
    # try
    # except
    # finally
    # raise: Allow to raise own exception
    
try:
    pass
except Exception as e:
    print(e)
else:
    print("Did not thown exception")
finally:
    print("Always execute")
    
# raise exception
def throw_exception(num):
    if(num == 0): raise Exception("Number 0 is not supported")
    else: print(num)

try:
    throw_exception(1)
except Exception as e:
    print(e)
else:
    print("Exception not thrown")
finally:
    print("Done")    
