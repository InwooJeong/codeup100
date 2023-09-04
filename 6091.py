while True:
    print("방문 주기를 공백을 두고 입력하세요.(100 이하의 자연수)")
    a, b, c = map(int, input().split())
    
    d = 1
    
    isA = 1<=a<=100
    isB = 1<=b<=100
    isC = 1<=c<=100
    
    if isA and isB and isC:
        
        while d%a!=0 or d%b!=0 or d%c!=0:
            d+=1
        
        print(d)
        break
    else:
        print("입력값을 확인하세요.")