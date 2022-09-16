# 튜플과 함수 : 튜플을 리턴할 수 있다. -> 여러 값을 리턴받을 수 있다.

# 함수 선언
def test():
    return 10, 20


# 여러 개의 값을 리턴받음
a, b = test()

# 출력
print('a:', a)
print('b:', b)
