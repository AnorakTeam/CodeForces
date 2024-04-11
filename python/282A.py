n = int(input())

arr = []

for i in range(n):
    arr.append(input().replace("X", ""))

x = 0

for operation in arr:
    if operation == "++":
        x += 1
    else:
        x -= 1

print(x)
