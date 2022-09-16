# 반복문으로 파일 한줄씩 읽기
with open('info.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # 변수 선언
        name, weight, height = line.strip().split(', ')

        # 데이터 정합성 체크
        if (not name) or (not weight) or (not height):
            continue
        # 결과 계산
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ''
        if 25 <= bmi:
            result = '과체중'
        elif 18.5 <= bmi:
            result = '정상 체중'
        else:
            result = '저체중'

        # 출력
        print('\n'.join([
            "이름: {}",
            '몸무게: {}',
            '키: {}',
            'BMI: {}',
            '결과: {}'
        ]).format(name, weight, height, bmi, result))
        print()
