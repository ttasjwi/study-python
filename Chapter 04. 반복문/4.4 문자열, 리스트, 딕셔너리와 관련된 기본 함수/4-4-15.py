# 반복할 수 있는 것 : 이터러블
# - 리스트, 딕셔너리, 문자열, 튜플 등
#
# 이터러블 중에서, next()를 통해 하나하나 꺼낼 수 있는 것 : 이터레이터

# 변수 선언
numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)

# reversed_numbers : r_num
print('reversed_numbers : ', r_num)
print(next(r_num)) # for문에서 이터레이터를 넘기면 next를 호출해서 반복한다
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
