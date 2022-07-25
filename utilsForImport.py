def add(*args):
    if(len(args) == 2): return args[0] + args[1]
    result = 0
    for x in args:
        result += x
    return result

def multiply(*args):
    if(len(args) == 2): return args[0] * args[1]
    result = 0
    for x in args:
        result *= x
    return result
