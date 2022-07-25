# file handling
    #open, read, write/create, delete
    #mode=> r(read), a(append), w(write, overwrite), 
    # x(create, create speicific file)
    # remove(remove file)
    
    #if not exist, return error

#IMP: use with keyword to avoid file.close()

import readline


with open("sample.txt", "w") as f:
    f.write("some lines of code")
        
with open("sample.txt", "r") as f:
    for l in f.readlines():
        print(l)