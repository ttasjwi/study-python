# 리스트 컴프리헨션(List comprehensions), 리스트 내포

# 변수 선언
array = []

# 반복문 사용
for i in range(0, 19 + 1, 2):
    array.append(i ** 2)

# 출력
print(array)
print()

# 동일한 표현 (리스트 컴프리헨션 적용)
array = [i * i for i in range(0, 19 + 1, 2)]
print(array)
print()

# 조건 적용
array = [i * i for i in range(0, 19 + 1) if i % 2 == 0]
print(array)
