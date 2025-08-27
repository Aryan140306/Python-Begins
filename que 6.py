s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter number of characters to swap: "))

# Check if n is valid
if n > len(s1) or n > len(s2):
    print("Error: n is larger than the length of one of the strings.")
else:
    # Swap first n characters
    new_s1 = s2[:n] + s1[n:]
    new_s2 = s1[:n] + s2[n:]

    print("\nAfter swapping first", n, "characters:")
    print("String 1:", new_s1)
    print("String 2:", new_s2)