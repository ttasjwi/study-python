class Human:
    def __init__(self) -> None:
        pass


class Student(Human):
    def __init__(self) -> None:
        pass


## 학생 선언
student = Student()

## 인스턴스 확인
print('isinstance(student, Human):', isinstance(student, Human))  # True
print('type(student):', type(student) == Human)  # True

