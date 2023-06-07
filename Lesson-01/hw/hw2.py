#def asterisk_triangle(n):
    #for i in range(n):
        #for j in range(i, n):
            #print("",end="")
        #for j in range(i+1):
            #print("*",end="")
        #for j in range(i+1):
            #print("*",end="")
        #print("\r")
#n = 9
#asterisk_triangle(n)


n = 9
for i in range(n):
    for j in range(i, n):
            print('',end='')
    for j in range(i+1):
            print('*',end='')
    for j in range(i+1):
            print('*',end='')
    print()

for i in range(n):
    print((10+1) * " ", 1 + "*", 1 + "*")