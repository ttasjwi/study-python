list_number = [52, 273, 32, 72, 100]

try:
    # 숫자 입력
    number_input = int(input('점수 입력 > '))

    # 리스트 요소 출력
    print('{}번째 요소 : {}'.format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as e:
    print('정수를 입력해주세요')
    print(type(e), e)
except IndexError as e:
    print('리스트의 인덱스를 벗어났어요')
    print(type(e), e)
except Exception as e:
    print('미리 파악하지 못 한 예외가 발생했습니다.')
    print(type(e), e)
