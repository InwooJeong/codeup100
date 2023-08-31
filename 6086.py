while True:
    print("100,000,000 이하의 정수를 하나 입력하세요.")
    num = int(input())
    
    isNum = 1<=num<=100,000,000
    now = 0
    sum = 0
    
    if isNum:
        
        while True:
            sum += now
            now += 1
            if sum>=num:
                break
        
        print(sum)
        break
    else:
        print("입력값을 확인하세요.")
        continue