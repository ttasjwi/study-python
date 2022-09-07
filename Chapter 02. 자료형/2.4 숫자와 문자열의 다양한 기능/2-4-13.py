# 문자열 찾기 : find() , rfind()
# java의 indexOf 와 구조적으로 비슷한 것 같다.

# find : 앞에서부터 찾아서 문자열이 처음 시작하는 인덱스를 반환
# rfind : 뒤에서부터 찾아서 문자열이 처음 시작하는 인덱스를 반환


str = "안녕안녕하세요"
print(f"str = {str}")
print("str.find(\"안녕\") = {}".format(str.find("안녕")))
print("str.rfind(\"안녕\") = {}".format(str.rfind("안녕")))
