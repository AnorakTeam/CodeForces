n = input()
string  = input()
answer = 0
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        answer += 1

print(answer)