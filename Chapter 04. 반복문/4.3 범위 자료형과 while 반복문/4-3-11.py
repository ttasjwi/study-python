# break(탈출)

# 변수 선언
i = 0

# 무한 반복
while True:
    # 반복 횟수 출력
    i += 1
    print(f'{i} 번째 반복문 입니다.')


    # 종료 조건을 묻는다.
    input_text = input('> 종료하시겠습니까? (y/n): ')
    if input_text in ['y', 'Y']:
        print('반복을 종료합니다.')
        break

