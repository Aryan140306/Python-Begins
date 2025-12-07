import math   # To use sqrt() for distance calculation

class Point:
    def __init__(self, x, y):
        self.x = x          # Store x coordinate
        self.y = y          # Store y coordinate

    def __str__(self):
        return f"({self.x}, {self.y})"  # String format of the object

    def distance(self, other):
        # Formula: √[(x2 - x1)² + (y2 - y1)²]
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)


# ---- Taking inputs ----
x1 = float(input("Enter x for point 1: "))
y1 = float(input("Enter y for point 1: "))

x2 = float(input("Enter x for point 2: "))
y2 = float(input("Enter y for point 2: "))

# Creating Point objects
p1 = Point(x1, y1)
p2 = Point(x2, y2)

# Printing objects
print("Point 1 is:", p1)
print("Point 2 is:", p2)

# Calculating distance
d = p1.distance(p2)
print("Distance between two points =", d)
