
# 딕셔너리에 요소 제거
# del 딕셔너리['key]

dictionary = {
    'name': '7D 건조 망고',
    'type': '당절임'
}

# 요소 제거 전에 내용을 출력해본다
print('요소 제거 이전:', dictionary)

# 딕셔너리 요소 제거
del dictionary['name']
del dictionary['type']

# 요소 제거 후에 내용을 출력
print('요소 제거 이후:', dictionary)
