# def modify_list(list):
#     list.append(8)

# lst=[10,20,30]
# modify_list(lst)
# print(lst)

# def modify_tuple(t):
#     t=t+(4,)

# t=(1,2,3)
# modify_tuple(t)
# print(t)

def modify_tuple(t):
    return t + (4,)

t = (1, 2, 3)
t = modify_tuple(t) # Reassigning the global variable
print(t) # Output: (1, 2, 3, 4)