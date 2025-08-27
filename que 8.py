# Input list with different types
data = [1, 2, 'hello', 4, 7.5, 6, '9', 10]

cubes = []
for x in data:
    if isinstance(x, int) and x % 2 == 0:   # check integer and even
        cubes.append(x ** 3)

print("Cubes using for loop:", cubes)
