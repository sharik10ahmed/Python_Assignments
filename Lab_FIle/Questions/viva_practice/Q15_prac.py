import sys

def si(principal,rate=5,time=2):
    return (principal*rate*time)/100
if len(sys.argv) == 3:
   print("Command line detected")
   num1 = float(sys.argv[1])
   num2 = float(sys.argv[2])
   print(f"sum of {num1} and {num2} is {num1+num2}")
   print()
   
while True:
   print("Main Menu")
   print("1.Sum and multiplication")
   print("2.Calculate SI-> ")
   print("3.Calculate SI with custom-> ")
   print("Exit")
   choice = int(input("Enter choice-> "))
   
   if choice == 1:
      a = int(input("Enter num1-> "))
      b = int(input("Enter num1-> "))
      print("Sum is ",a+b)
      print("product is ",a*b)
   elif choice == 2:
      p = int(input("Enter principal-> "))
      result= si(p)
      print("SI -> ",result)
   elif choice == 3:
      p = int(input("Enter principal-> "))
      r = int(input("Enter rate-> "))
      t = int(input("Enter time-> "))
   
      result= si(p,r,t)
      print("SI(custom)-> ",result)
   elif choice == 4:
      print("Exiting program !")
      break
   else:
      print("Invaild choice!")
       

      
