matrix = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
max_index = []

for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max_num:
            max_num = matrix[i][j]
            max_index = [i , j ]
print(max_num)
print(max_index[0] + 1, max_index[1] + 1)