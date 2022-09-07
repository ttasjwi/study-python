
# 문자열.upper() : 대문자화 결과를 반환
# 문자열.lower() : 소문자화 결과를 반환
# 주의 : side effect 없다.

original = "Hello Python Programming...!"
upper = original.upper() # upper 함수는 side effect가 없다. (원본 문자열을 변화시키지 않음)
lower = original.lower()

print(f"original = {original}")
print(f"upper = {upper}")
print(f"lower = {lower}")
