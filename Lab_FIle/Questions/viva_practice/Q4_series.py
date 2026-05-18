sum=0
n = int(input("Enter a number-> "))
for i in range(1,n+1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
        
print(f"sum of terms upto {n}-> {sum}")
