n = int(input())
total_people = 0
min_capacity = 0
for i in range(n):
    leaving_passagers, entering_passagers = list(map(int, input().split()))
    total_people += (entering_passagers - leaving_passagers)
    if total_people > min_capacity:
        min_capacity = total_people

print(min_capacity)
    