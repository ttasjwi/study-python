# try - except- else 구문
try:
    radius = int(input('정수 입력> '))
except:
    print('정수를 입력하지 않았습니다.')
else:
    print('원의 반지름:', radius)
    print('원의 둘레:', radius * 2 * 3.14)
    print('원의 넓이:', (radius **2) * 3.14)

