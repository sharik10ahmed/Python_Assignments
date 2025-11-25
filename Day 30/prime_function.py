def prime_check(a,b):
    for i in range(a,b):
      if i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
               is_prime = False
               break
        if is_prime==True:
            print(i, end=' ')
v1 = int(input("Enter First -> "))
v2 = int(input("Enter Second-> "))
print(f"Even no. from {v1} and {v2}:- ")
prime_check(v1,v2)