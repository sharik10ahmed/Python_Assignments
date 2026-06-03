try:
     num = int(input("Enter a number-> "))
     ans = 10/num
     print("result: ",ans)
except ValueError:
     print("Enter numbers only")
except ZeroDivisionError:
     print("error cannot divide by zero")
