# 튜플을 리턴하는 함수의 예

print('# 반복문에서 반복 대상을 2개 둘 수 있는 경우가 있는데 이 또한 튜플이다.')
for i, value in enumerate([1, 2, 3, 4, 5, 6]):  # (i, value)는 튜플이다.
    print('{}번째 요소는 {}입니다.'.format(i, value))
print()

a, b = 97, 40
print('# 튜플의 형태로 반환하는 대표적인 함수는 divmod(a,b)가 있다.')
print(a, b)
share, remainder = divmod(a, b)
print('몫 :', share)
print('나머지', remainder)
