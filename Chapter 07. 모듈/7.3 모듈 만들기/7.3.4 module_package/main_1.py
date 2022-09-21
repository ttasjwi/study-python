from test_package import *

print(module_a.variable_a)
print(module_b.variable_b)
# print(module_c.variable_c) : __all__에서 지정하지 않은 모듈은 사용할 수 없다
# 패키지를 가져올 때 __init__을 제일 먼저 실행함을 알 수 있다
# 파이썬 3.3부터는 __init__ 없이도 패키지가 작동함
