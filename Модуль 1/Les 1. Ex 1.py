n = int(input())
arr = list(map(int, input().split(' ')))

for i in range(n):
    x = arr[i]
    j = i
    while j > 0 and arr[j - 1] > x:
        arr[j] = arr[j - 1]
        j -= 1
        arr[j] = x

print(' '.join(map(str, arr)))