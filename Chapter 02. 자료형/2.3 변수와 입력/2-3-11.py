
# 실습
raw_input = input('inch 단위의 숫자를 입력해주세요: ')

# 입력받은 데이터를 숫자 자료형으로 cm로 변경, cm 단위로 변경
inch = int(raw_input) # int로 형변환
cm = inch * 2.54 # cm

# 출력
print(inch, "inch는 cm단위로", cm,'cm입니다.')
