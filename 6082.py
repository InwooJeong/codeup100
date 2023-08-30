num = int(input())

clap = [3,6,9]

for i in range(1, num+1):
    if i%10 in clap:
        print("X", end=' ')
    else:
        print(i, end=' ')