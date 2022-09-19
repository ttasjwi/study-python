# 파이썬 메모리 구조
# 1. 스택 : 전역 스택, 함수 스택
# 2. 스택에는 기본 데이터 타입의 경우 평가된 값이 저장되고, 객체 데이터 타입은 힙 메모리의 주소 참조값이 저장된다
# 3. 힙 : 객체 데이터가 실제로 저장됨
# 4. 함수의 매개변수에는 기본 데이터 타입의 경우 평가된 값이 복사되어 전달되고, 객체 데이터 타입의 경우 참조값이 복사되어 저장된다.

def number_function(a): # 함수의 변수에 값이 복사됨(call by value)
    a += 10
    print('local_variable a =', a)


def list_function(b): # 함수의 참조 변수에 참조값이 복사됨(call by value)
    b[0] = 'd'
    print('local_variable b=', b)


a = 30 # 기본 자료형 : 스택에 평가된 값이 저장됨
b = ['a', 'b', 'c'] # 객체 자료형 : 스택에 참조(힙에 위치한 객체 주소)가 저장됨

print('global a=', a)
number_function(a)
print('global a=', a)
print()

print('global b=', b)
list_function(b)
print('global b =', b)
print()
