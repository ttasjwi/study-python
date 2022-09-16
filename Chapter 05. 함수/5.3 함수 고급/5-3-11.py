# 파일을 열고, 닫기
# open(파일 경로, 모드)
# 모드
#  - 1. 'w' : write - 새로 쓰기
#  - 2. 'a' : append - 뒤에 이어서
#  - 3. 'r' : read - 읽기 모드

file = open('basic.txt', 'w')

file.write('Hello Python Programming...!')

file.close()
