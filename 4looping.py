#for
#while
#continue
#break

num = [x for x in range(0, 10)]
for x in num:
    print(x, end=", ")
    
for x in num:
    if(x == 3):
        break
    else:
        print(x)

for x in num:
    if(x == 3):
        continue
    else:
        print(x)
    
a = 0        
while a <= 10:
    print(a)
    a +=1         
