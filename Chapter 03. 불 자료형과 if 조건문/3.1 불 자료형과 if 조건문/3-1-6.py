# 계절을 구분하는 프로그램
import datetime

now = datetime.datetime.now()
month = now.month

season = ''

if 3 <= month <= 5:
    season = '봄'

if 6 <= month <= 8:
    season = '여름'

if 9 <= month <= 11:
    season = '가을'

if 1 <= month <= 2 or season == 12:
    season = '겨울'

print('이번 달은 {}월로 {}입니다!'.format(month, season))
