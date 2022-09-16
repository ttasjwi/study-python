# 랜덤한 숫자를 만들기 위해 가져온다.
import random

# 간단한 한글 리 스트를 만든다.
hanguls = list('가나다라마바사아자차카타파하')

# 파일을 쓰기 모드로 연다.
with open('info.txt', 'w', encoding='utf-8') as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성한다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        # 텍스트를 쓴다.
        file.write('{}, {}, {}\n'.format(name, weight, height))
