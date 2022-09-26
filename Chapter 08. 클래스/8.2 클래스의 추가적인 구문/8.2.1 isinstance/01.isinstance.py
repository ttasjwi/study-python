
# 어떤 클래스의 인스턴스인지 확인하기

class Student:
    def __init__(self) -> None:
        pass

# 학생 선언
student = Student()

# 인스턴스 확인하기 (클래스 인스턴스 또는 하위 클래스 인스턴스인가?)
print('isinstance(student, Student):', isinstance(student, Student))

