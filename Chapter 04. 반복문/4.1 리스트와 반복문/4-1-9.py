# 값으로 제거하기 (remove : 처음 발견된 요소부터 제거한다.)
list_c = [1, 2, 1, 2]
print('list_c = ', list_c)

list_c.remove(2)
print('list_c.remove(2) -> list_c = ', list_c)

list_c.remove(0)
# 없는 요소를 지우려고 하면 ValueError 발생
