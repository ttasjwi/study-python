
# 가변 매개변수 뒤에 디폴트 매개변수를 선언했을 때

def print_n_times(*values: str, n: int = 2):
    # n번 반복합니다.
    for i in range(n):
        # values들 기준으로 반복합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()


# 함수 호출
print_n_times('안녕하세요', '즐거운', '프로그래밍', 3)
# 가변 매개변수 뒤에 디폴트 매개변수를 선언하면 가변 매개변수가 우선시 된다.
# 디폴트 매개변수가 적용은 되지만, 덮어 씌는게 개발자 뜻대로 되지 않는다.
