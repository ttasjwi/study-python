# 람다: lambda 매개변수: 리턴값

# 함수 선언
power = lambda x: x * x
is_under_3 = lambda x: x < 3

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]
print('# list_input_a')
print(list_input_a)
print()

# map() 함수 사용
output_a = map(power, list_input_a)
print('# map() 함수 실행 결과')
print('map(power, list_input_a):', output_a)
print('map(power, list_input_a):', list(output_a))
print()

output_b = filter(is_under_3, list_input_a)
print('# filter() 함수의 실행 결과')
print('# filter(is_under_3, list_input_a):', output_b)
print('# filter(is_under_3, list_input_a):', list(output_b))
