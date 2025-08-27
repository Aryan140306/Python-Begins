import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other):
        """Calculate distance between two points"""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


#
