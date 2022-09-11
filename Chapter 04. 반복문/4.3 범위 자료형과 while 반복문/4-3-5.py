# 별 찍기 1

n: int = int(input('줄 수 입력: '))
string_builder = []

for i in range(1, n+1): # 1 ~ n 줄까지
    for j in range(i): # 매줄마다 i개의 별을 쌓는다
        string_builder.append('*')
    string_builder.append('\n')

answer = str.join('', string_builder).rstrip()
print(answer, end='')
