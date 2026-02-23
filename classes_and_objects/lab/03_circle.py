class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius) -> None:
        self.radius = new_radius

    def get_area(self) -> float:
        return self.pi * self.radius * self.radius

    def get_circumference(self) -> float:
        return self.pi * 2 * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
