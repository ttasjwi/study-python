
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'

    def __eq__(self, other):
        return self.get_sum() == other.get_sum()

    def __ne__(self, other):
        return self.get_sum() != other.get_sum()

    def __gt__(self, other):
        return self.get_sum() > other.get_sum()

    def __ge__(self, other):
        return self.get_sum() >= other.get_sum()

    def __lt__(self, other):
        return self.get_sum() < other.get_sum()

    def __le__(self, other):
        return self.get_sum() <= other.get_sum()


# 학생들을 선언
student_a, student_b = Student('윤인성', 87, 98, 88, 95),\
                       Student('연하진', 92, 98, 96, 98)
print('이름', '총점', '평균', sep='\t')
print(str(student_a))
print(str(student_b))

# 학생들을 비교
print('student_a == student_b = ', student_a == student_b)
print('student_a != student_b = ', student_a != student_b)
print('student_a > student_b = ', student_a > student_b)
print('student_a >= student_b = ', student_a >= student_b)
print('student_a < student_b = ', student_a < student_b)
print('student_a <= student_b = ', student_a <= student_b)
