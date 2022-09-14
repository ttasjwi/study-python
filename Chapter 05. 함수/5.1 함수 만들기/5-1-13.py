# 기본적인 함수의 활용

def sum_all(start: int, end: int) -> int:
    sum = 0
    for i in range(start, end+1):
        sum += i

    return sum

print(f'0 to 100 = {sum_all(0, 10)}')
print(f'0 to 1000 = {sum_all(0, 1000)}')
print(f'50 to 100 = {sum_all(50, 100)}')
print(f'500 to 1000 = {sum_all(500, 1000)}')
