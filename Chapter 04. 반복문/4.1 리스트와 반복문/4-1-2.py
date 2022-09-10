# 리스트 접근 연산자를 2,3,... 중 사용 가능
list_a = [273, 32, 103, '문자열', True, False]
print(list_a[3][0])  # 리스트의 요소 -> 문자열 인덱싱

list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["문자열", "으악"]]
print(list_a[1])
print(list_a[1][1])
print(list_a[3][1][1])
