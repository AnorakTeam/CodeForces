n, k = input().split()

n = int(n)
k = int(k)

arr = list(map(int, input().split()))

kth_score = arr[k - 1]

answer = 0

""" 
# pense que funcionaria, pero yo ser tonto aun :,)
if(kth_score > 0):
    answer += k
    for i in range(k, n):
        if arr[i] != kth_score:
            break
        answer += 1 """

# toco fuerza bruta, f
for i in range(n):
    if arr[i] != 0 and arr[i] >= kth_score:
        answer += 1;
    else:
        break


print(answer)