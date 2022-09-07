
# 입력
number = int(input('정수 입력 >'))

# 조건문
kind = None
if number % 2 == 0:
    kind = '짝수'
else:
    kind = '홀수'

print('{}입니다.'.format(kind))
