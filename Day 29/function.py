def even_check(a,b):
    // this code is run by sharik ahmad
    
    for i in range(a,b):
        if i%2==0:
           print(i,end='')
           print(" ",end='')
x = int(input("Enter starting range -> "))
y = int(input("Enter ending range-> "))

print(f"Even no. from {x} and {y}:- ")
even_check(x,y)