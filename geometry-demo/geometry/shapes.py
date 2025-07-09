from abc import ABC, abstractmethod
import math
class Shape(ABC): 
    def area(self) -> float:
        pass
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self) -> float:
        return self.side **2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self) -> float:
        return math.pi* self.radius **2
    

    