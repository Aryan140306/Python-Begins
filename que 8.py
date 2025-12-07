# Create a user-defined list using for loop 
lst = eval(input("Enter a list: "))

cubes = []   # to store cubes of even integers

for item in lst:
    if isinstance(item, int) and item % 2 == 0:
        cubes.append(item ** 3)

print("Cubes of even integers =", cubes)

# Create a user-defined list using list comprehension
lst = eval(input("Enter a list: "))

cubes = [item**3 for item in lst if isinstance(item, int) and item % 2 == 0]

print("Cubes of even integers =", cubes)
