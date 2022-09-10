# False으로 변환되는 값
# - None, 숫자 0, 0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)
# - 나머지는 True로 변환된다.
# - (자바를 학습한 입장에선 이 사용법이 매우 극혐이다...)

print('# if 조건문에 0 넣기')
if 0:
    print('0은 True로 변환될까요?')
    print(' ')
else:
    print('0은 False로 변환됩니다')
    print(' ')

print('# if 조건문에 빈 문자열 넣기')
if "":
    print('빈 문자열은 True로 변환될까요?')
else:
    print('빈 문자열은 False로 변환됩니다')
