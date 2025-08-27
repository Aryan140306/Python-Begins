n = int(input("Enter the number of rows: "))

# Pyramid
print("Pyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Reverse Pyramid
print("\nReverse Pyramid:")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
