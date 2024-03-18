i = int(input())
arr = list(map(int, input().split(' ')))
n = int(input())

for el in arr:
    if el == n:
        i -= 1

print(i)