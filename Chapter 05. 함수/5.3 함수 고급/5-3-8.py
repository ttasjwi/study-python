# map(함수, 리스트) : 함수를 적용한 것들을 map object형태(제너레이터)로 반환
# filter(불리언 함수, 리스트) : 불리언 함수의 리턴값이 True인 것들로만 filter object형태(제너레이터)로 변환

# 함수 선언
def power(item):
    return item * item


def is_under_3(item):
   return item < 3


# 변수 선언
print('# list_input_a')
list_input_a = [1,2,3,4,5]
print(list_input_a)
print()

# map() 함수를 선언
output_a = map(power, list_input_a)
print('# map() 함수 실행 결과')
print('map(power, list_input_a):', output_a)
print('map(power, list_input_a):', list(output_a))
print()

# filter() 함수 사용
output_b = filter(is_under_3, list_input_a)
print('# filter() 함수의 실행 결과')
print('# filter(is_under_3, list_input_a):', output_b)
print('# filter(is_under_3, list_input_a):', list(output_b))
