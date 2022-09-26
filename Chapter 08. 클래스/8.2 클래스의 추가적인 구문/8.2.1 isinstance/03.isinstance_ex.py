def main() -> None:
    classroom = [Student(), Student(), Teacher(), Student(), Student()]
    for person in classroom:
        do_something(person)


def do_something(person) -> None:
    if isinstance(person, Student):
        person.study()
        return
    elif isinstance(person, Teacher):
        person.teach()
        return


class Student:
    def study(self) -> None:
        print('공부를 해요.')


class Teacher:
    def teach(self) -> None:
        print('학생을 가르칩니다.')


if __name__ == '__main__':
    main()
