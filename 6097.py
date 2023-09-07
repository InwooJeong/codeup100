while True:
    h, w = map(int, input('세로, 가로 크기를 입력하세요.(1~100)\n').split())
    
    if 1>w or w>100 or 1>h or h>100:
        print('1~100만 유효합니다!')
        continue
    
    n = int(input('놓을 수 있는 막대 개수를 입력하세요.(1~10)\n'))
    
    if 1>n or 10<n:
        print('1~10사이!')
        continue
    
    grid = [[0 for col in range(w)] for row in range(h)]
    
    for i in range(n):
        l,d,x,y = map(int, input(f'{i+1}번째 막대 길이, 방향, X, Y 값을 입력하세요.\n').split())
        
        x -= 1
        y -= 1
        
        # 가로 세로가 배열로 생각하고 값을 증가 시켜줘야 모양이 나온다.
        for i in range(l):
            # 가로
            if d == 0:
                grid[x][y+i] = 1
            # 세로
            if d == 1:
                grid[x+i][y] = 1
    
    for x in range(h):
        for y in range(w):
            print(grid[x][y],end = ' ')
        print()    
        
    break