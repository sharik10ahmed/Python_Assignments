def max_max_val(n):
    max_val= n[0]
    for num in n:
        if num > max_val:
            max_val = num
    return max_val
v=input("Enter Number just add spaces -> ")
string=v.split()
my_max_val=[]
for i in string:
    numbers= int(i)
    my_max_val.append(numbers)
result = max_max_val(my_max_val)
print(f"Largest number -> {result}")