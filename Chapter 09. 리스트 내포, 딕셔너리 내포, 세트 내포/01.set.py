a = {1, 2, 3}
b = {2, 3, 4}
c = {1, 1, 1, 2, 2, 2}
d = set()

print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합
print(b - a)
print(a ^ b)  # 대칭 차집합 (교집합 제외 나머지 합집합)
print(c)
