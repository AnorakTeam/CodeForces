n = int(input())

arr = []

for i in range(n):
    arr.append(input())

solved_problems = 0

for options in arr:
    if sum(map(int, options.split())) > 1:
        solved_problems += 1

print(solved_problems)
