
# 디폴트 매개변수, 키워드 매개변수를 활용하여 정수 더하는 함수
def sum_all(start: int = 0, end: int = 100, step:int = 1) -> int:
    sum = 0
    for i in range(start, end+1, step):
        sum += i
    return sum


print('A.', sum_all(0, 100, 10))
print('B.', sum_all(end=100))
print('C.', sum_all(end=100, step=2))
