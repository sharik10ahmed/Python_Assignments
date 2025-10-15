# Tag_list = TL
T_L = [12,24,45,22,77,77,77,90]
T_L.append(35) # adds a value in last
print(T_L)
T_L.extend([45,567,87])
print(T_L) # adds multiple values at last 
T_L.insert(2,89)
print(T_L) # inserts a value on a specified index
T_L.remove(12)
print(T_L) # remove a value
T_L.pop(-2)
print(T_L) # deletes last term by default or specified term
o = T_L.index(77)
print(o) # tells the index value of specified value
op = T_L.count(77)
print(op) # counts the no. of occurence of specified value
T_L.sort()
print(T_L) # sorts values in ascending and descending
T_L.reverse()
print(T_L) # reverse value from opposite
New_List = T_L.copy()
print(T_L) # just copies a list to a variable
print(New_List)