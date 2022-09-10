# 리스트 내부에 값이 있는지/없는지 확인하기

list_a = [273, 32, 103, 57, 52]
print('list_a = ', list_a)
print()

# 값 in 리스트 : 값이 있는지 여부를 반환
print('273 in list_a = ', 273 in list_a)
print('99 in list_a = ', 99 in list_a)
print('100 in list_a = ', 100 in list_a)
print('273 in list_a = ', 273 in list_a)
print('52 in list_a = ', 52 in list_a)
print()

# 값 not in 리스트 : 값이 없는지 여부를 반환
print('273 in list_a = ', 273 not in list_a)
print('99 in list_a = ', 99 not in list_a)
print('100 in list_a = ', 100 not in list_a)
print('52 in list_a = ', 273 not in list_a)
print('not 273 in list_a = ', not 273 in list_a) # bad
print()
