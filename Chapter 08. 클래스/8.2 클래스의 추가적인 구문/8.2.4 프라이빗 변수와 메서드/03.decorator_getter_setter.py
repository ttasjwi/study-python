import math


class Circle:
    def __init__(self, radius) -> None:
        Circle.__validate_radius(radius)
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, update_radius):
        Circle.__validate_radius(update_radius)
        self.__radius = update_radius

    @classmethod
    def __validate_radius(cls, radius):
        if radius <= 0:
            raise TypeError("반지름은 양수여야합니다.")


circle = Circle(10)
print('# 원의 둘레와 넓이를 구합니다.')
print('원의 둘레:', circle.get_circumference())
print('원의 넓이:', circle.get_area())

## 원의 __radius에 간접적으로 접근
print('# __radius에 간접적으로 접근')
print(circle.radius)

# 원의 둘레와 넓이를 구합니다.
circle.radius = 2
print("# 반지름을 변경하고, 원의 둘레와 넓이를 구합니다.")
print("원의 둘레 :", circle.get_circumference())
print("원의 둘레 :", circle.get_area())
