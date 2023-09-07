while True:
    n = int(input("놓일 흰돌의 개수를 입력하세요.(1~10)\n"))
    table = [[0 for j in range(19)]for i in range(19)]
    isOK = 'O'
    stones = []
    chkStones = []
    
    if n<1 or n>10:
        print("흰돌은 1개에서 10개 사이로 놓입니다.")
        continue
    
    for i in range(n):
        x, y = map(int, input(f'{i+1}번째 흰 돌의 좌표 : x y\n').split())
        stones.append([x,y])
        
        if x<1 or x>19 or y<1 or y>19:
            print('바둑판은 19*19 사이즈!')
            isOK = 'N'
            break
        
        table[x-1][y-1] = 1
        
    for stone in stones:
        if stone not in chkStones:
            chkStones.append(stone)

    if len(stones)!= len(chkStones):
        isOK = 'N'
        print('같은 위치에 돌을 둘 수 없습니다.')
        continue
    
    if isOK == 'N':
        continue
    
    for i in range(19):
        for j in range(19):
            print(table[i][j],end=' ')
        print()
        
    break