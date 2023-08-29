class Point:
    color = 'blue'

    def __init__(self, point_a, point_b):
        self.__point_a = point_a
        self.__point_b = point_b

    @property
    def point_a(self):
        return self.__point_a

    @property
    def point_b(self):
        return self.__point_b

    @point_a.setter
    def point_a(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.__point_a = value

    @point_b.setter
    def point_b(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.__point_b = value

    def draw(self):
        print(f" drawing from point {self.__point_a} to {self.__point_b}")

    def __str__(self):
        return f"({self.__point_a}, {self.__point_b}"

    def __eq__(self, other):
        return self.__point_a == other.point_a and self.__point_b == other.point_b


Point.color = 'red'
p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1.point_a)
print(p2.color)
xy = p1.point_a + p2.point_a
zy = p2.point_b + p2.point_b
print(xy)
print(zy)
