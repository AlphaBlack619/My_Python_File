class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print(f"drawing from point{self.a} to {self.b} ")

    def __str__(self):
        return f"{self.a} to {self.b} "
