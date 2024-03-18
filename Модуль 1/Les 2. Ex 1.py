i = int(input())
arr = list(map(int, input().split(' ')))
n = int(input())

k = 0

for el in arr:
    if el == n:
        k += 1

print(k)