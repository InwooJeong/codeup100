while True:
    print("시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)을 공백을 두고 입력하세요.(a,m,d ~50~50, 0<n<=10)")
    a, m, d, n = map(int, input().split())
    
    isA = -50<=a<=50
    isM = -50<=m<=50
    isD = -50<=d<=50
    isN = 1<=n<=10
    
    if isA and isM and isD and isN:
        
        cnt = 1
        
        while cnt<n:
            a=a*m+d
            cnt+=1
        print(a)    
        break
    else:
        print("입력값을 확인하세요.")