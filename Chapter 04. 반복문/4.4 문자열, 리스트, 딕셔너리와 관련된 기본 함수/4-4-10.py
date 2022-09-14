# if 문 안에서 긴 문자열 선언(bad)

number = int(input('정수 입력 > '))

# if 조건문
if number %2 == 0:
    print("입력한 문자열은 {}입니다.\n{}은(는) 짝수입니다.".format(number, number))

else:
    print("입력한 문자열은 {}입니다.\n{}은(는) 홀수입니다.".format(number, number))
