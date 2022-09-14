# 매개변수 갯수가 맞지 않을 경우, TypeError 발생

def print_n_times(value: str, n: int): # 매개변수는 2개
    for i in range(n):
        print(value)

print_n_times('안녕하세요', 5)
print_n_times('안녕하세요') # TypeError
print_n_times('안녕하세요', 5, '나나나') # TypeError
