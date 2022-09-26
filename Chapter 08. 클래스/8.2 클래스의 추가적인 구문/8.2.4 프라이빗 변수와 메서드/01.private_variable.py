import math


class Circle:
    def __init__(self, radius) -> None:
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)
print('# 원의 둘레와 넓이를 구합니다.')
print('원의 둘레:', circle.get_circumference())
print('원의 넓이:', circle.get_area())

## 원의 __radius에 접근
print('# 원의 __radius에 접근합니다.')
print(circle.__radius)

