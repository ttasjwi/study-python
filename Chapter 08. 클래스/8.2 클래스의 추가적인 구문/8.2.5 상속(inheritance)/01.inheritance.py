class Parent:
    def __init__(self):
        self.value = '테스트'
        print('Parent 클래스의 __init()__ 메서드가 호출되었습니다.')

    def test(self):
        print('Parent 클래스의 test() 메서드입니다.')


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print('Child 클래스의 __init()__ 메서드가 호출되었습니다.')


child = Child()
child.test()
print(child.value)
