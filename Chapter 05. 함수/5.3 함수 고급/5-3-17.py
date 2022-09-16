def test():
    print('A 지점 통과')
    yield 1
    print('B 지점 통과')
    yield 2
    print('C 지점 통과')


# 함수 호출
output = test()
print('D 지점 통과')
a = next(output)
print(a)

print('E 지점 통과')
b = next(output)
print(b)

print('F 지점 통과')
c = next(output)
print(c)

# 제너레이터에서 더 이상 반환할 수 없을 경우 StopIteration 예외 발생
next(output)
