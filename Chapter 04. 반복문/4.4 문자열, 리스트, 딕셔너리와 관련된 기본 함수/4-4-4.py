
# enumerate(...)

example_list = ['요소A', '요소B', '요소C']

i = 0
print('# 변수를 별도로 할당해서 인덱스 추적')
for item in example_list:
    print(f'{i}번 요소는 {item}입니다.')
    i += 1
print()

print('# range(...) 함수를 통해 인덱스 기반으로 요소 접근')
for i in range(len(example_list)):
    print(f'{i}번 요소는 {example_list[i]}입니다.')
print()

print(enumerate(example_list))
print(type(enumerate(example_list)))

tmp = enumerate(example_list)

for i, value in tmp: # enumerate : 인덱스, 정보를 같이 가지는 반복자 객체
    print(f'{i}번 요소는 {value}입니다.')
print()

for i, value in tmp: # 이미 소모됐으므로 사용하지 못 함
    print(f'{i}번 요소는 {value}입니다.')
print()
