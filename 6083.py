while True:
    print("r, g, b 색상을 공백으로 띄워 입력하세요.(0~127 사이의 값)")
    r, g, b = map(int, input().split())
    
    isR = r>=0 and r<=127
    isG = 0<=g<=127
    isB = 0<=b<=127
    cnt = 0
    
    if isR and isG and isB:
        # print("조건 만족")
        
        for i in range(r):
            for j in range(g):
                for k in range(b):
                    print(i, j, k)
                    cnt += 1
        print(cnt)
        break
    else:
        print("다시 입력하세요.")
        continue