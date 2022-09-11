# 딕셔너리
dict_a = {
    "keyA": 10, # 문자열을 key로 사용하기
    "keyB": 20,
    "keyC": 5,
    1: 40, # 숫자를 key로 사용하기
    False: 50 # 불을 key로 사용하기
}

print(dict_a)
print(dict_a['keyA'])

dict_b = {
    'director': ['안소니 루소', '조 루소'],
    'cast': ['아이언맨', '타노스', '토르', '닥터스트레인지', '헐크']
}
print(dict_b)
print(dict_b['director'])
print(dict_b['cast'][2])
