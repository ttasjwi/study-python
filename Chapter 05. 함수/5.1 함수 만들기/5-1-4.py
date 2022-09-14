# 가변 매개변수
# *변수명 : 가변 매개변수 선언
# 1. 가변 매개변수를 선언한 뒤에는 일반 매개변수가 올 수 없다.
# 2. 가변 매개변수는 단 하나만 선언할 수 있다.

def print_n_times(n: int, *values: str):
    # n번 반복합니다.
    for i in range(n):
        # values에 속한 value들마다
        for value in values:
            print(value)
        print()  # 단순한 줄바꿈


# 함수 호출
print_n_times(3, '안녕하세요', '즐거운', '파이썬 프로그래밍')
