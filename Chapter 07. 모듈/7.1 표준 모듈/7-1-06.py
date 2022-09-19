# sys : 시스템과 관련된 정보를 제공하는 모듈
import sys

# 명령 매개변수 출력
print(sys.argv)
print('----------')

# 컴퓨터 환경과 관련된 정보 출력
print('getwindowsversion:()', sys.getwindowsversion()) # 윈도우 버전
print('----------')

print('copyright:', sys.copyright) # 파이썬 저작권 정보
print('----------')

print('version :', sys.version)

# 프로그램 강제 종료
sys.exit()
