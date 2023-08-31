while True:
    print("0~100 사이 정수 3개를 공백을 두고 입력하세요.")
    a, d, n = map(int, input().split())
    
    isA = 0<=a<=100
    isD = 0<=d<=100
    isN = 0<=n<=100
    
    if isA and isD and isN:
        for i in range(n-1):
            a += d
        print(a)
        break
    else:
        print("입력값을 확인하세요")
        continue