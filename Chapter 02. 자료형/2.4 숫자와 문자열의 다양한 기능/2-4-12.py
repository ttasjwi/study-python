
# 문자열의 구성 파악하기 : isOO

str = 'abc123'
print(f"str = {str}")
print(f"str.isalnum() = {str.isalnum()}") # isalnum() : 문자열이 알파벳 또는 숫자로 구성됐는 지 여부 반환
print()

str = 'abc'
print(f"str = {str}")
print(f"str.isalpha() = {str.isalpha()}") # isalpha() : 문자열이 알파벳으로만 구성되어 있는지 여부를 반환
print()

str = 'True'
print(f"str = {str}")
print(f"str.isidentifier() = {str.isidentifier()}") # isidentifier() : 문자열이 식별자로 사용될 수 있는 것인지 여부를 반환
print()

str = '123'
print(f"str = {str}")
print(f"str.isdecimal() = {str.isdecimal()}") # isdecimal() : 문자열이 정수 형태인지 확인
print()

str = '1234f'
print(f"str = {str}")
print(f"str.isdigit() = {str.isdigit()}") # isdigit() : 문자열이 숫자로 인식될 수 있는 것인지 확인
print()

str = '    '
print(f"str = {str}")
print(f"str.isspace() = {str.isspace()}") # isspace() : 문자열이 공백으로만 구성되어 있는지 확인
print()

str = 'aaa'
print(f"str = {str}")
print(f"str.islower() = {str.islower()}") # islower() : 문자열이 소문자로만 구성되어 있는지 확인
print()

str = 'aaa'
print(f"str = {str}")
print(f"str.isupper() = {str.isupper()}") # isupper() : 문자열이 대문자로만 구성되어 있는지 확인
