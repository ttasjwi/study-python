# operator.itemgetter : 특정 필드를 추출하는 함수를 만드는 함수

from operator import itemgetter

books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 10000
}, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 20000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]


print('# 가장 저렴한 책')
print(min(books, key=itemgetter('가격')))
print()

print('# 가장 비싼 책')
print(max(books, key=itemgetter('가격')), end='')
