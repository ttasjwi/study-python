# 딕셔너리.items() : 재사용 가능, key, value의 형태로 반복자 호출 가능

# 변수 선언
example_dictionary = {
    '키A': '값A',
    '키B': '값B',
    '키C': '값C',
}

# 딕셔너리의 items() 함수 결과 출력
print('# 딕셔너리의 items() 함수')
print(example_dictionary.items())
print()

items = example_dictionary.items()

# for문과 items() 조합
print('# 딕셔너리의 items()와 for 반복문 조합')
for key, value in items:
    print('dictionary[{}] = {}', key, value)
print()

print('# 재사용 가능')
for key, value in items:
    print('dictionary[{}] = {}', key, value)
print()
