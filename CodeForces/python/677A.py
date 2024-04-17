n, h = list(map(int, input().split()))

friends = list(map(int, input().split()))

width = 0
for friend in friends:
    if friend <= h:
        width += 1
    else:
        width += 2

print(width)