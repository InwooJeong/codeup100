while True:
    n = int(input("출석 번호를 부른 횟수를 입력하세요."))
    
    if n<1 or n>10000:
        print("입력값을 확인하세요.")
        continue
    
    num = list(map(int, input(f'{n}개의 수를 입력하세요.').split()))
    
    if len(num) != n:
        print("입력숫자 수를 확인하세요.")
        continue
    
    minimun = num[0]
    
    for i in num:
        minimun = min(i, minimun)
    
    print(minimun)
    break