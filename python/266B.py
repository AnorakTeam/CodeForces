n, t = list(map(int, input().split()))
children = list(input())

for _ in range(t):
    i = 0
    while i < n-1:
        if children[i] == "B" and children[i+1] == "G":
            children[i], children[i+1] = children[i+1], children[i]
            i += 1
        i += 1
        
order = ""
for i in children:
    order += i
    
print(order)