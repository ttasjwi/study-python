# 리스트에 요소 추가

print('# 리스트')
list_a = [1, 2, 3]
print('list_a =', list_a)
print()

print('# 리스트 뒤에 요소 추가하기 : append (Side Effect 있다.)')
list_a.append(4)
list_a.append(5)
print('list_a.append(4)')
print('list_a.append(5)')
print('list_a =', list_a)
print()

print('# 리스트 중간에 요소 추가하기 : insert (Side Effect 있다, 뒤로 밀려난다)')
list_a.insert(0, 10)
print('list_a.insert(0, 10)')
print('list_a =', list_a)
print()

print('# 리스트 뒤에 여러 요소 추가하기 : extend (Side Effect 있다.)')
list_a.extend([6, 7, 8, 9, 0])
print('list_a.extend([6, 7, 8, 9, 0])')
print('list_a = ', list_a)
