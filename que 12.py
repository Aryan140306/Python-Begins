
# Given tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values in one line and the other half in the next line
half = len(t1) // 2
print("First half:", t1[:half])
print("Second half:", t1[half:])

# b. Create another tuple of even numbers (separate code block)
even_numbers = []
for x in t1:
    if x % 2 == 0:
        even_numbers.append(x)

even_tuple = tuple(even_numbers)
print("Even numbers tuple:", even_tuple)

# c. Concatenate tuple t2 with t1
t2 = (11, 13, 15)
new_tuple = t1 + t2
print("Concatenated tuple:", new_tuple)

# d. Find maximum and minimum value
print("Maximum value:", max(new_tuple))
print("Minimum value:", min(new_tuple))
