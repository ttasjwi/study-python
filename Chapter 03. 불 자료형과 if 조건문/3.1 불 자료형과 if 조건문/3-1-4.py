# import 문 : 날짜/시간과 관련된 기능을 가져온다.
import datetime

# 현재 날짜, 시간을 구한다.
now = datetime.datetime.now()

# 출력
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond

print(f'{year}년 {month}월 {day}일 {hour}시 {minute}분 {second}초 {microsecond}마이크로초')
