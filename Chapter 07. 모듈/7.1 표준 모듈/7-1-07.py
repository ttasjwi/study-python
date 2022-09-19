# os 모듈 : 운영체제 관련 기능 제공
import os

# 기본 정보를 몇 개 출력
print('현재 운영체제 :', os.name) # 운영체제
print('현재 폴더:', os.getcwd()) # 현재 폴더(current working directory)
print('현재 폴더 내부의 요소:', os.listdir()) # 현재 폴더 내부 요소

# 폴더를 만들고 제거(폴더가 비어있을 때만 제거 가능)
os.mkdir('hello')
os.rmdir('hello')

# 파일 생성, 파일 이름 변경
with open('original.txt', 'w', encoding='utf-8') as file:
    file.write('hello')
os.rename('original.txt', 'new.txt')

# 파일 제거
os.remove('new.txt')

# 시스템 명령어 실행
os.system('dir')
