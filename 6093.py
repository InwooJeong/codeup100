while True:
    n = int(input("출석 번호를 부른 횟수를 입력하세요.(1~1000)"))
    
    if n<1 or n>1000:
        print("입력값을 확인하세요.")
        continue
    
    num = list(map(int, input(f'{n}개의 수를 입력하세요.').split()))
    
    pro = 'y'
    for i in range(n):
        if num[i]>23 or num[i]<1:
            print('1~23 사이의 수를 입력하세요!')
            pro = 'n'
            break
    
    for i in reversed(num):
        print(i, end=' ')    
        
    
    if pro=='n':
        continue
    else:
        break