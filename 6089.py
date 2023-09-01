while True:
    print("시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)을 공백을 두고 입력하세요.(모두 0~10)")
    a, r, n = map(int, input().split())
    A=[]
    
    isA = 0<=a<=10
    isR = 0<=r<=10
    isN = 0<=n<=10
    
    if isA and isR and isN:
        
        cnt = 1
        
        while cnt < n:
            A.append(a)
            cnt += 1
            a = a*r
        print(A)    
        print(a)    
        break
    else:
        print("입력 값을 확인하세요")
        continue