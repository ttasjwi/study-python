list_a = [1,2,3,4,5]
list_reversed = reversed(list_a) # reverseiterator로 받는다

print(list_a)
print(type(list_reversed)) # <class 'list_reverseiterator'>
print(list_reversed) # <list_reverseiterator object at 0x000002237EDE65C0>
print(list(list_reversed)) # 이터레이터가 소모된다.
print()

for element in reversed([1,2,3,4,5]):
    print('-', element)
