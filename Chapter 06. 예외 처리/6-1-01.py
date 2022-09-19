try:
    # 입력
    radius = int(input('반지름을 입력> '))  # 예외 발생 가능성이 있음

    # 출력
    print('원의 반지름:', radius)
    print('원의 둘레:', 2 * 3.14 * radius)
    print('원의 넓이:', 3.14 * (radius ** 2), end='')

except :
    print('무언가 잘못됐습니다.', end='')
