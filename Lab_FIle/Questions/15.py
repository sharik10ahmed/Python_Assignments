import sys

def calculate_si(principal,rate=5.0,time=2.0):
    return (principal*rate*time) / 100
if len(sys.argv) ==3:
       print("math detected")
       num1 = float(sys.argv[1])
       num2 = float(sys.argv[2])
       print(f"Addition of {num1} and {num2} = {num1 + num2}")
       print("-----------------------------------\n")
while True:
       print("===Main Menu===")
       print("1. Perform Multiplication and Addition")
       print("2. SI with default rate=5 and time=2")
       print("3. SI with custom p,r,t")
       print("4. EXIT")
       choice = input("Enter your choice(1-4): ")
       if choice == '1':
          a = float(input("Enter num1-> "))
          b = float(input("Enter num2-> "))
          print(f"-> Addition: {a+b}")
          print(f"-> Multiplication {a*b}")
       elif choice == '2':
          p = float(input("Enter principal-> "))
          interest = calculate_si(p)
          print(f"SI is {interest}")
       elif choice == '3':
          p = float(input("Enter principal-> "))
          r = float(input("Enter rate-> "))
          t = float(input("Enter time-> "))
          interest = calculate_si(p,r,t)
          print(f"SI for custom values-> {interest}")
       elif choice == '4':
          print("Exitng the program")
          break
       else:
          print("Invalid choice ! select from 1 to 4")
       
