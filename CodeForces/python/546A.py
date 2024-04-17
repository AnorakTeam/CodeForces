k, m, w = list(map(int, input().split()))

total_cost = k*w*(w + 1) / 2

if total_cost >= m:
    print(int(total_cost - m))
else:
    print(0)
