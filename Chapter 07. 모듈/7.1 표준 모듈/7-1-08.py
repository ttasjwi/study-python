# datetime 모듈
from datetime import datetime

print('#  현재 시각을 구하고 출력하기')
now = datetime.now()
print(now.year, '년')
print(now.month, '월')
print(now.day, '일')
print(now.hour, '시')
print(now.minute, '분')
print(now.second, '초')
print()

print('# 시간으 포맷에 맞춰 출력하기')
output_a = now.strftime('%Y.%m.%d %H:%M:%S')
print(output_a)
output_b = f'{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초'
print(output_b)
output_c = now.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초')
print(output_c)
