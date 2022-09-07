# 입력을 받는다
number = int(input('정수 입력> '))

# 양수 조건
if number > 0:
    print('양수입니다.')

# 음수 조건
if number < 0:
    print('음수입니다.')

# 0 조건
if number == 0:
    print('0입니다.')

# 조건문 indent는 공백 4개인데, pycharm은 이를 탭으로 4글자 인덴트를 준다.
