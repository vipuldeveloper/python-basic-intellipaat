
# Declare list and print
num = [1, 2, 3, 4]
print(num)

num.append(5)
print(num)

x = num.pop(1)
print(x)
print(num)

for x in num:
    print(x)
print("Done")    


# Dictionary 
sal = {
    "vipul": 14,
    "Tushar": 23
}
sal['Andy'] = 30
#print(sal.get("Andy"))

for key, val in sal.items():
    print(key)
    print(val)
    
print("Andy" in sal)


# set
s = {1, 2, 3}
print(type(s))