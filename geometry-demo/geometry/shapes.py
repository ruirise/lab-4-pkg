from abc import ABC, abstractmethod
import math
class Shape(ABC): 
    def area(self) -> float:
        pass
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self) -> float:
        if(self.side < 0):
            raise ValueError("sides can't be negative")
        return self.side **2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self) -> float:
        if(self.radius < 0):
            raise ValueError("sides can't be negative")
        return math.pi* self.radius **2
    

    