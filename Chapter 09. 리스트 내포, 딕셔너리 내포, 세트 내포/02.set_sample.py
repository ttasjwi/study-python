participants = ['가 고등학교', '나 고등학교', '다 고등학교', '가 고등학교', '다 고등학교', '다 고등학교', '라 고등학교']

set1 = set()
for school in participants:
    set1.add(school)

set2 = set()
set2.update(participants)

set3 = set(participants)

print(f'set1 = {set1}, {len(set1)}개 학교')
print(f'set2 = {set2}, {len(set2)}개 학교')
print(f'set3 = {set3}, {len(set3)}개 학교')
