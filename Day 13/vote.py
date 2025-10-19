try:
   age = int(input("Enter Your Age -> "))
except ValueError:
   print("Invaild response")
   exit()
if age > 105:
   print("Invalid response")
   exit()
if age < 18:
   print("Your not eligible to vote !")
else:
     Citizenship = input("Enter Your Nationality -> ")
     if Citizenship.lower() == "indian":
      print("You are eligible to vote")
     else:
        print("You are not Eligible to Vote")
   
   
    
   