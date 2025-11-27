d=0
try:
   n = int(input("Enter Positive Integer -> "))
except ValueError:
   print("Invalid Response")
   exit()
if n==1:
    print("No")

for i in range(2,n):
    if n%i==0:
        d=1
        break

if d==0:
    print("yes\n")
else:
    print("No")
