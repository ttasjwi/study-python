import random

print('# random 모듈')

# random() : 0.0 <= x < 1.0 사이의 float 리턴
print('- random() :', random.random())

# uniform(min, max) : min 이상 max 이하의 float 리턴
print('- uniform(10, 20) :', random.uniform(10, 20))

# randrange(stop) : 0<= 값 <= max-1
# randrange(min, stop) : min <= 값 <= max-1
# randrange(min, stop, step) : min <= 값 <= max-1, step씩 증가
print('- randrange(10):', random.randrange(10))

# randint(min, max): min 이상 max 이하
print('- randint(3,5):', random.randint(3, 5))

# choice(list) : 리스트 내부 요소를 랜덤하게 선택
print('- choice([1,2,3,4,5]):', random.choice([1,2,3,4,5]))

# shuffle(list) : 리스트 내부의 요소를 랜덤하게 섞음. 반환 x
print('- shuffle([1,2,3,4,5]):', random.shuffle([1,2,3,4,5]))

# shuffle(list) : 리스트의 요소 중에 k개를 뽑습니다.
print('- sample([1,2,3,4,5], k=2):', random.sample([1,2,3,4,5], k=2))

