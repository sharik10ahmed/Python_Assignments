# Given tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a) Print contents of t1 in 2 separate lines (half on each line)
mid = len(t1) // 2
print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# b) Print all even values of t1 as another tuple t2
t2 = tuple(x for x in t1 if x % 2 == 0)
print("Tuple of even values t2:", t2)

# c) Concatenate a tuple t3 = (11,13,15) with t1
t3 = (11, 13, 15)
t_concat = t1 + t3
print("After concatenation:", t_concat)

# d) Return maximum and minimum value from t1
max_val = max(t1)
min_val = min(t1)
print("Maximum value in t1:", max_val)
print("Minimum value in t1:", min_val)
