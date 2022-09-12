# continue: 다음으로

# 변수 선언
numbers = [5, 15, 6, 20, 7, 25]

# 반복(10 이상인 수만 출력)
for number in numbers:
    if number < 10:
        continue
    # 출력
    print(number)
