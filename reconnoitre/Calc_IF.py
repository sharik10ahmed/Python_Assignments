user_input = ""
while user_input.lower() != "close":
import os
os.system('cls')
import math
try:
   print("Calculator Ver.1.1".center(160))
   u1 = int(input("1.Addition\n2.Difference\n3.Product\n4.Division\n5.Floor Division\n6.Exponential\n\n\nSelect Your Choice -> "))
   n1 = int(input("Enter 1 No. -> "))
   n2 = int(input("Enter 2 No. -> "))
except ValueError:
    print("Invalid response")
    exit()
    
if u1 == 1:
    print("Addition -> ",n1+n2)
if u1 == 2:
    print("Difference -> ",n1-n2)
if u1 == 3:
    print("Product -> ",n1*n2)
if u1 == 4:
    print("Division -> ",n1/n2)
if u1 == 5:
    print("Floor Division -> ",math.trunc(n1//n2))
if u1 == 6:
    print("Exponential -> ",n1**n2)






