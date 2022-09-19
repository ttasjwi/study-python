# pass 키워드 : 해당 구문을 스킵

# 변수 선언
list_input_a = ['52', '273', '32', '스파이', '103']

# 반복 적용
list_number = []
for element in list_input_a:
    try:
        float(element)
        list_number.append(element)
    except:
        pass

# 출력
print('{} 내부에 있는 숫자는'.format(list_input_a))
print('{}입니다.'.format(list_number))
