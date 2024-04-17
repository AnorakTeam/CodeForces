string = sorted(list(map(int, input().split(sep="+"))))
correct_string = ""

for i in range(len(string)):
    correct_string += str(string[i]) + "+"
correct_string = correct_string[:len(correct_string)-1]

print(correct_string)
