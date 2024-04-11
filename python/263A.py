row_position = 0
column_position = 0
found = False

for i in range(5):
    row = list(map(int, input().split()))
    if not found:
        for j in range(5):
            if row[j] == 1:
                row_position = i+1
                column_position = j+1
                found = True
                break

moves = abs((3-row_position)) + abs((3-column_position))

print(moves)
