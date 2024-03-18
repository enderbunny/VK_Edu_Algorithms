n = int(input())
data = list(map(int, input().split(' ')))
res = ''

for i in range(1, n):
    if data[0] % 2 == 0 or data[i] % 2 == 0:
        data[0] += data[i]
        res += '+'
    else:
        data[0] *= data[i]
        res += 'x'
print(res)