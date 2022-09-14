# 리스트 평탄화를 하는 재귀함수

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item) # 재귀적으로 리스트 요소를 평탄화 시켜서, output에 추가함.
        else:
            output.append(item)
    return output


example = [[1, 2, 3], [4, [5, 6], 7, [8, 9]]]
print('원본 = {}'.format(example))
print('변환 = {}'.format(flatten(example)))
