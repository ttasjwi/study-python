
# 인덱스로 리스트 요소 제거하기
list_a = [0, 1, 2, 3, 4, 5]
print('list_a =',list_a)

# 제거방법 [1] - del 키워드 (인덱스로 제거)
del list_a[1]
print('del list_a[1] -> list_a = ', list_a)

# 제거방법 [2] - pop() 함수 (인덱스로 제거, 기본값 -1)
list_a.pop(2)
print('list_a.pop(2) -> list_a = ', list_a)
print()

# pop()은 기본적으로 맨 뒤 요소를 제거한다
list_a.pop()
print('list_a.pop() -> list_a = ',  list_a)
