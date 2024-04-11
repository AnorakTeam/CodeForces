n = int(input())

arr = []

for i in range(n):
    arr.append(input())

for word in arr:
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word[1:-1])) + word[-1])