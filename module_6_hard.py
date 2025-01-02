class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = bool
    def __init__(self, sides_count, __sides, __color, filled):
        self.sides_count = sides_count
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return r, g, b
        else:
            return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = self.filled

    def __is_valid_sides(self, *args):
        for side in self.__sides:
            if len(self.__sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return self.__sides * self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            self.sides_count

class Circle(Figure):
    sides_count = 1
    __radius = None

    def get_square(self):
        radius = self.__sides[0]
        return 3.1415926 * radius ** 2

class Triangle(Figure):
    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

class Cube(Figure):
    sides_count = 12
    __sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    def get_volume(self):
        return self.__sides * 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube(12, [1]*12, [222, 35, 130], True)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())













