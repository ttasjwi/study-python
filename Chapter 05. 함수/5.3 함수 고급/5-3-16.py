# 제너레이터 객체

def test():
    print('함수가 호출되었습니다.')
    yield 'test' # 반환을 미룸


# 함수 호출
print('A 지점 통과')
test()

print('B 지점 통과')
test()
print(test()) # 제너레이터 객체
