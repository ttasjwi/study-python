# 키가 존재하는지 확인 : 키 in 딕셔너리
# 키가 존재하지 않는지 확인 : 키 not in 딕셔너리

# 딕셔너리 선언
dictionary = {
    'name': '7D 건조 망고',
    'type': '당절임',
    'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
    'origin': '필리핀'
}

print('\'name\' in dictionary : ', 'name' in dictionary)
print('\'type\' not in dictionary : ', 'type' not in dictionary)

# 사용자로부터 입력을 받는다.
key = input('> 접근하고자 하는 키: ')

# 출력
if key in dictionary:
    print(dictionary[key])
else:
    print('존재하지 않는 키에 접근하고 있습니다.')
