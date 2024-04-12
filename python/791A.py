"""Bear and Big Brother"""

limak, bob = input().split()

limak = int(limak)
bob = int(bob)
years = 0

while limak <= bob:
    limak *= 3
    bob *= 2
    years += 1

print(years)

"""
x*3*limak > x*2*bob
3*limak / (2*bob) > 1
      wtf ??
"""