original = [1, 2, 3, 4, 5]

list_comprehension = [str(i) for i in original]  # 선 생성
generator_expression = (str(i) for i in original)  # 실행 시점에 생성

# 원본 수정
original[0] = 100
print(', '.join(list_comprehension))
print(', '.join(generator_expression))
