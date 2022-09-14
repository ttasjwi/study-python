
numbers = [1,2,3,4,5]

tmp = reversed(numbers) # list_reverseiterato는 소모된다

for i in tmp:
    print('첫번째 반복문', i)

for i in tmp:
    print('두번째 반복문', i) # 출력 안 됨

tmp = reversed(numbers) # 재할당

for i in tmp:
    print('세번째 반복문', i) # 출력 됨
