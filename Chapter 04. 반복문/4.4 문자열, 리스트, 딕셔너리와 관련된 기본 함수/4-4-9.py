# 인덴트가 적용되는 '문' 안에서 여러줄 문자열을 선언 (2) 출력은 정상인데 코드는 이상


number = int(input('정수 입력 > '))

# if 조건문
if number %2 == 0:
    print('''입력한 문자열은 {}입니다.
{}은(는) 짝수입니다.'''.format(number, number))

else:
    print('''입력한 문자열은 {}입니다.
{}은(는) 홀수입니다.'''.format(number, number)) # if, else 문의 indent가 여러줄 문자열에 적용됨...

