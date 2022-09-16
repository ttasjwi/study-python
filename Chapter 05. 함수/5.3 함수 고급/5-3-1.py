# 튜플의 선언 및 인덱싱

# 튜플 선언 및 데이터 접근
tuple_test = (10, 20, 30)
print(tuple_test[0])
tuple_test[1] = 30  # 내부 값 변경 불가 / TypeError: 'tuple' object does not support item assignment

# 요소가 하나뿐인 튜플은 마지막에 콤마를 써야함
tuple_test = (30,)
print(tuple_test[0])
