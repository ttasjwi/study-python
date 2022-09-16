# 람다를 인수로 바로 전달

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]
print('# list_input_a')
print(list_input_a)
print()

# map() 함수 사용
output_a = map(lambda x: x * x, list_input_a)
print('# map() 함수 실행 결과')
print('map(power, list_input_a):', output_a)
print('map(power, list_input_a):', list(output_a))
print()

output_b = filter(lambda x: x < 3, list_input_a)
print('# filter() 함수의 실행 결과')
print('# filter(is_under_3, list_input_a):', output_b)
print('# filter(is_under_3, list_input_a):', list(output_b))
