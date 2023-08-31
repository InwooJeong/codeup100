while True:
    
    print("h, b, s, c 값을 공백으로 띄워 입력하세요.")
    
    h, b, c, s = map(int, input().split())

    isH = 0<h<=48000
    isB = b%8==0 and 0<b<=32
    isC = 0<c<=5
    isS = 0<s<=6000
    
    if isH and isB and isC and isS:
        print("{:0.1f}".format(h*b*c*s/8/1024/1024), "MB")
        break
    else:
        print("유효값을 확인하고 입력하세요.")
        continue