from geometry import Shape, Circle, Square, area_stats
a = [Circle(2),Circle(3),Square(4),Square(9)]
for i in a:
    print(f"Area is {i.area()}")
print(area_stats(a))
