class Student:
    # 생성자 (생성 시점에 실행)
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        print('{} - 생성되었습니다.'.format(self.name))

    # 소멸자(소멸되기 직전 실행)
    def __del__(self):
        print('{} - 파괴되었습니다.'.format(self.name))

# 학생 리스트 선언
students = [
    Student('윤인성', 87, 98, 88, 95),
    Student('연하진', 92, 98, 96, 98),
    Student('구지연', 76, 96, 94, 90),
    Student('나선주', 98, 92, 96, 92),
    Student('윤아린', 95, 98, 98, 98),
    Student('윤명월', 64, 88, 92, 92)
]


# Student 인스턴스의 속성에 접근하는 방법
print(students[0])
print(type(students[0]))
print(students[0].name)
print(students[0].korean)
print(students[0].math)
print(students[0].english)
print(students[0].science)
