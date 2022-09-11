# 별 찍기 2

n: int = int(input('줄 수 입력: '))
string_builder = []

for i in range(1, n + 1):
    for j in range(n - i):
        string_builder.append(' ')

    for k in range(2 * i - 1):
        string_builder.append('*')

    string_builder.append('\n')

answer = str.join('', string_builder).rstrip()
print(answer, end='')
