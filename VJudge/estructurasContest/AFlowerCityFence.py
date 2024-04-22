t = int(input()) #numero de casos
for _ in range(t):
    n = int(input())
    fences = list(map(int, input().split()))
    
    # si no es cuadrada, entonces ya nos la pela este test
    if n != fences[0]:
        print("NO")
        continue

    flipped = []

    #dio mio, bendito sea python
    #básicamente, para hacer esta "inversa de la adjunta", se puede 
    #conseguir añadiendo al nuevo arreglo elementos de la siguiente forma:
    #empezamos con el mayor número posible de cercas (n), y lo añadiremos 
    #el número de veces que encontremos al lado contrario del arreglo (fences[i])
    #(en papel se explica mejor, tbh) 
    for i in range(n, 0, -1):
        while len(flipped) < fences[i - 1]:
            flipped.append(i)

    """
    #pasó que todo este bloque es O(n²), no me alcanzó el tiempo, f
    #de todas formas, funciona :p
    #basicamente le va restando 1 cuadricula a todos y las va sumando en orden al arreglo
    #flipped, cuando un numero se vuelve cero es que ya no tiene mas cuadriculas por quitar
    #toncs se popea y se sigue sumando al siguiente hasta cubrir todo el "fences" original 

    #hacemos una copia para modificar el original
    copia = origen.copy()
    #donde estara la matriz volteada, todo inicia en cero
    flipped = [0 for _ in range(len(origen))]

    for i in range(len(origen)):
        fence = 0
        limit = len(copia)
        while fence < limit:
            if copia[fence] > 0:
                flipped[i] += 1
                copia[fence] -= 1
            else:
                copia.remove(copia[fence])
                limit -= 1

            fence += 1
    """
    
    if fences == flipped:
        print("YES")
    else:
        print("NO")

