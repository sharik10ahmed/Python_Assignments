def divi(a,b):
    for i in range(a,b):
        if i%10 == 0:
            print(i,end='')
            print(" ",end='')
v1 = int(input("Enter First -> "))
v2 = int(input("Enter Second-> "))
divi(v1,v2)