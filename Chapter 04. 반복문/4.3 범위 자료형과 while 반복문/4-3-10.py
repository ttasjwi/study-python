import time

# 조건 기반 반복

# time.time() : 1970년 1월 1일 0시 0분 0초로부터 몇 초가 경과했는 지 반환

count = 0
target_tick = time.time() + 5 # 5초 이후의 시간

# 5초간 반복
while time.time() < target_tick:
    count += 1

# 출력
print(f'5초 동안 {count}번 반복했습니다.')
