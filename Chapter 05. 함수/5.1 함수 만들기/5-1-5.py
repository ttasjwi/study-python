# 디폴트 매개변수(Default Parameter)
# 기본값으로 넣어줄 디폴트 인자를 지정 가능
# 물론, 인자로 다른 값을 넘기면 덮어씌울 수 있다

def print_n_times(value: str, n: int = 2):
    # n번 반복한다.
    for i in range(n):
        print(value)
    print()

print_n_times('안녕하세요')
print_n_times('안녕 못 해', 3)
