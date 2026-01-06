matrix = [
    [1, 2, 3],
    [4, 1, 2],
    [5, 4, 1]
]

rows = len(matrix)
cols = len(matrix[0])


is_toeplitz = True
for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][j] != matrix[i-1][j-1]:
            is_toeplitz = False

is_symmetric = True
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False


max_sum = 0
max_row = 0
for i in range(rows):
    if sum(matrix[i]) > max_sum:
        max_sum = sum(matrix[i])
        max_row = i


rotated = []
for c in range(cols):
    row = []
    for r in range(rows - 1, -1, -1):
        row.append(matrix[r][c])
    rotated.append(row)

print("Toeplitz:", is_toeplitz)
print("Symmetric:", is_symmetric)
print("Row with max sum:", max_row)
print("Rotated Matrix:")
for r in rotated:
    print(r)
