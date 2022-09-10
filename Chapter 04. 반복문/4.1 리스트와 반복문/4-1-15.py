# n중 for문

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for items in list_of_list:
    print(items)
    for item in items:
        print(item)

# 활용례 2
for i in range(1, 3):
    for j in range(1, 3):
        print('(i,j) = ({}, {})'.format(i, j))
