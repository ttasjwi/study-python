
# 딕셔너리에 값 추가
# -  dictionary['key'] = value
# - key가 이미 존재하면 덮어쓰고, 없으면 새로운 key, value를 추가함

dictionary = {} # 딕셔너리 선언
print('요소 추가 이전:', dictionary)

# 딕셔너리에 요소 추가
dictionary['name'] = '새로운 이름'
dictionary['head'] = '새로운 정신'
dictionary['body'] = '새로운 몸'

# 출력
print('요소 추가 이후:', dictionary)
