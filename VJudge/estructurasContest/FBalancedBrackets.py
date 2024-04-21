from collections import deque

opening_brackets = ["(", "[", "{"]
closing_brackets = [")", "]", "}"]

t = int(input())

for _ in range(t):
    sequence = input()
    order = deque()
    is_valid = True

    if len(sequence) == 0:
        print("YES")
        continue

    
    for bracket in sequence:
        # si es de opening, lo agregamos sin problema
        if bracket in opening_brackets:
            order.append(bracket)
        

        if bracket in closing_brackets:
            pos = closing_brackets.index(bracket)
            
            # por si se vacia, pero hay un bracket de cierre (ya no hay de oppening)
            if len(order) == 0:
                is_valid = False
                break
            
            # buscamos el equivalente de opening, y lo comparamos con el ultimo de la deque
            # si no son iguales (ej. en order el ultimo es [ y se recibe un } toncs ya esta mal)
            if opening_brackets[pos] != order.pop():
                is_valid = False
                break
    
    # por si quedan sobrando brackets de opening,
    if len(order) == 0:
        if is_valid:
            print("YES")
        else:
            print("NO")
    #no esta vacio el order, toncs quedo sobrando un opening y ya esta mal
    else:
        print("NO")
