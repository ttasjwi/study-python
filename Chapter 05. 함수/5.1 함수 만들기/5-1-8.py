# 가변 매개변수 뒤에 디폴트 매개변수를 선언했을 때 - 키워드 매개변수 기능을 사용하라.

def print_n_times(*values: str, n: int = 2):
    # n번 반복합니다.
    for i in range(n):
        # values들 기준으로 반복합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()


# 함수 호출
print_n_times('안녕하세요', '즐거운', '프로그래밍', n=3)
# 가변 매개변수 뒤에 디폴트 매개변수를 선언했을 경우, 키워드 매개변수를 이용하여 매개변수를 지정하고 인자를 넘길 수 있다.
