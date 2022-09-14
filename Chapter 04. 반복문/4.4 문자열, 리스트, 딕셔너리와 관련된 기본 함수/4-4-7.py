# 리스트 컴프리헨션

array = ['사과', '자두', '초콜릿', '바나나', '체리']

output = [fruit
          for fruit in array
          if fruit != '초콜릿']

# 출력
print(output)
