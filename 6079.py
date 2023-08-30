n = int(input())
sum = 0

for i in range(0, 1001):
    sum += i
    
    if sum >= n:
        break
    
print(i)