while True:
    print("w, h, b 값을 공백을 두고 입력하세요. (단, 모두 정수이고 w와 h는 1~1024, b는 40이하 4의 배수)")
    w, h, b = map(int, input().split())
    
    isW = 1<=w<=1024
    isH = 1<=h<=1024
    isB = b<=40 and b%4==0
    
    if isW and isH and isB:
        print("{:0.2f}".format(w*h*b/8/1024/1024), "MB")
        break
    else:
        print("입력 조건을 확인하세요.")
        continue