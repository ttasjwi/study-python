
# 재귀함수
def factorial(k: int):
    if k == 0:
        return 1
    return k * factorial(k-1)


for i in range(1, 10 +1):
    print(f'{i}! = {factorial(i)}')

