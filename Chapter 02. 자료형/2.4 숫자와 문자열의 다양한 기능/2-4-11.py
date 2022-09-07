# 공백 제거
# strip : 양옆 공백, 무의미한 줄바꿈 제거
# lstrip : 왼쪽 공백, 무의미한 줄바꿈 제거
# rstrip : 오른쪽 공백, 무의미한 줄바꿈 제거

original = "   안녕하세요오오오오오   "

strip = original.strip()
l_strip = original.lstrip()
r_strip = original.rstrip()

print(f'original:{original}/끝')
print(f'strip:{strip}/끝')
print(f'lstrip:{l_strip}/끝')
print(f'rstrip:{r_strip}/끝')

lines = """
안녕하세요오오오
"""
print('-------------- 여러줄 -----------------')
print(lines)
print('------------ 여러줄 strip 후 무의미한 개행 제거 ------------')
print(lines.strip())
print('---------------------- 끝-----------------------')
