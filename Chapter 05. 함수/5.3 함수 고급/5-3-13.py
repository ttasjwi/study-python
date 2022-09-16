# read 함수 : 파일 읽기

with open('basic.txt', 'r') as file:
    # 파일을 읽고 출력
    contents = file.read()
print(contents)
