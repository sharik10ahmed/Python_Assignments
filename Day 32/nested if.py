your_pin = 4545
pin = int(input("Enter Pin-> "))
pin_correct= False
if pin==your_pin:
   pin_correct = True
balance = 1000

if pin_correct:
    print("PIN Accepted.")
    withdraw_amount = int(input("Enter Amount to withdraw -> "))
    
    if balance >= withdraw_amount:
        print("Dispensing Cash...")
    else:
        print("Insufficient Funds.")

elif pin_correct== False:
    print("Wrong PIN. Card Ejected.")