# del 키워드를 사용 시 슬라이싱으로, 리스트의 여러 요소를 한번에 제거할 수 있음
list_b = [0,1,2,3,4,5,6]
print('list_b = ', list_b)

del list_b[3:6]
print('del list_b[3:6] -> list_b = ', list_b)
print()

# [:end] : end 미포함 앞부분 제거
list_c = [0,1,2,3,4,5,6]
print('list_c = ', list_c)
del list_c[:3]
print('del list_c[:3] -> list_c = ', list_c)

# [start:] : start 포함 뒷부분 제거
list_d = [0,1,2,3,4,5,6]
print('list_d = ', list_d)
del list_d[3:]
print('del list_d[3:] -> list_d = ',list_d)
