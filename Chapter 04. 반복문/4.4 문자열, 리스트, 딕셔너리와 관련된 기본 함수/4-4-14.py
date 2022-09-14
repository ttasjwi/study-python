# if 문 안에서 긴 문자열 선언 - join을 통해 문자열 결합

number = int(input('정수 입력 > '))

# if 조건문
if number % 2 == 0:
    print('\n'.join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number, number))

else:
    print('\n'.join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number, number))
