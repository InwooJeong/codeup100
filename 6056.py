a, b = map(int, input().split())
c, d = bool(a), bool(b)

result = c and not d or not c and d
print(result)