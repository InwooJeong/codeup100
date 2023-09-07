column = []
for i in range(19):
    column.append([])
    column_input = input().split()
    for j in range(19):
        column[i].append(int(column_input[j]))

n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x)-1, int(y)-1

    for j in range(19):
        if column[x][j] != 0:
            column[x][j] = 0
        else:
            column[x][j] = 1

        if column[j][y] != 0:
            column[j][y] = 0
        else:
            column[j][y] = 1

for i in range(19):
    for j in range(19):
        print(column[i][j], end=" ")
    print()