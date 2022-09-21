# 시간 처리

# 모듈 읽기
from datetime import datetime, timedelta

now = datetime.now()
print('# 현재 시간')
print(now.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*"년월일시분초"))
print()

# 특정 시간 이후의 시간 구하기
print('# datetime.timedelta로 시간 더하기')
after = now + timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
print(after.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*"년월일시분초"))
print()

print('# now.replate()로 1년 더하기')
output = now.replace(year=(now.year + 1))
print(output.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*"년월일시분초"))
