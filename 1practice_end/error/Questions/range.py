import time

try:
# initializing a with range()
  a = range(0, 10000)

# initializing a with xrange()
  x = range(1, 10000)

# testing the type of a
  print("The return type of range() is : ")
  for i in a:
    print(a[i])
  print("\nPausing for 3 seconds...\n")
  time.sleep(3)
  print("\n")
  for i in x:
    print(x[i])

except Exception as e:
    print("Range Exceeded")
