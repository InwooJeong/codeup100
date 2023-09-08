# 미로 생성
maze = []
for i in range(10):
    maze.append([])
    for j in range(10):
        maze[i].append(0)
        
for i in range(10):
    a = input(f'미로{i+1} 번째 줄\n').split()
    for j in range(10):
        maze[i][j]= int(a[j])
        
# 개미 집 2,2 -> x,y로는 [1,1]
x = 1
y = 1
print('Result!---------------------------------------------------------')
while True:
    # 장애물이 없으면 -> 개미가 갔으니 9
    if maze[x][y] == 0:
        maze[x][y] = 9
    # 밥을 찾으면 -> 밥 찾았으니 9 주고 종료
    elif maze[x][y] == 2:
        maze[x][y] == 9
        break
    
    #개미 오른쪽, 왼쪽 모두 벽 or 개미가 미로 제일 오른쪽 아래에 도달 -> 종료
    if(maze[x][y+1]==1 and maze[x+1][y]==1) or (x==8 and y==8) :
        break
    
    #개미 이동 패턴
    if maze[x][y+1] != 1:
        y+=1
    elif maze[x+1][y] != 1:
        x+=1
        
for i in range(0,10):
    for j in range(0,10):
        print(maze[i][j], end=' ')
    print()