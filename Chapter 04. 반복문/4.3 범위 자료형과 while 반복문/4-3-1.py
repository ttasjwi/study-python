# 범위 자료형 : range(...)

# 매개변수 1개 : range(n) : 0~n-1만큼 반복(총 n회)
# 매개변수 2개 : range(a,b) : a~b-1까지 반복
# 매개변수 3개 : range(a,b, k) : a이상 b 미만까지 k씩 증가하면서 반복
# 범위 자료형을 인자로 하여, 리스트를 만들 수 있다

print(list(range(5))) # 0,1,2,3,4
print(list(range(1, 4+1))) # 1,2,3,4
print(list(range(1, 9+1, 2))) # 1,3,5,7,9

a = range(0, 10//2) # range 자료형의 인자는 정수만 올 수 있으니, 나머지 연산자 사용시 주의
print(list(a))
