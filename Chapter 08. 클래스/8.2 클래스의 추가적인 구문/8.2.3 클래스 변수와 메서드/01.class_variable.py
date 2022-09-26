class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print(f'{Student.count}번째 학생이 생성되었습니다.')

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return '{}\t{}\t{}'.format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

# 학생 리스트 선언
students = [
    Student('윤인성', 87, 98, 88, 95),
    Student('연하진', 92, 98, 96, 98),
    Student('구지연', 76, 96, 94, 90),
    Student('나선주', 98, 92, 96, 92),
    Student('윤아린', 95, 98, 98, 98),
    Student('윤명월', 64, 88, 92, 92)
]


# print('학생을 한 명씩 반복)
print(f'현재 생성된 총 학생 수는 {Student.count}명입니다.')
