while True:
    print("출석 번호를 부른 횟수 n을 입력하세요.(1~1000)")
    n = int(input())
    print(f"{n}개의 수를 띄워서 입력하세요.")
    
    num = list(map(int, input().split()))
    
    result = list(0 for i in range(24))
    isN = 1<=n<=1000
    isL = len(num) == n
    pro = 'ok'
    
    if isN and isL:
        for i in range(n):
            if num[i]>=24 or num[i]<1:
                print('출석 번호는 1~23!')
                pro = 'not'
                break
            else:    
                result[num[i]]+=1
        
        if pro=='not':
            continue
            
        for i in range(1,24):
            print(result[i], end=' ')
        
        break
    else:
        print("입력한 수를 확인하세요.")