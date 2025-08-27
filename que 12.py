# Given tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# (a) Print half the values of the tuple in one line and the other half in the next line
mid = len(t1) // 2
print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# (b) Print another tuple whose values are even numbers in the given tuple
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print("Tuple with even numbers:", even_tuple)

# (c) Concatenate a tuple t2=(11,13,15) with t1
t2 = (11, 13, 15)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# (d) Return maximum and minimum value from this tuple (t3)
print("Maximum value:",
