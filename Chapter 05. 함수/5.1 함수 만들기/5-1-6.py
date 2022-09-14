# 디폴트 매개변수가 가변 매개변수보다 앞에 올 때

def print_n_times(n: int = 2, *values: str):
    # n번 반복합니다.
    for i in range(n):
        # values들 기준으로 반복합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()


# 함수 호출
print_n_times('안녕하세요', '즐거운', '프로그래밍')
# TypeError : 디폴트 매개변수를 가변 매개변수 앞에 선언하면, 디폴트 매개변수의 의미가 사라진다.
