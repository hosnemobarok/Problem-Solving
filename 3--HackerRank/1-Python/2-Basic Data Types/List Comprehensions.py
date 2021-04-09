X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

Xi = [x for x in range(X+1)]
Yi = [y for y in range(Y+1)]
Zi = [z for z in range(Z+1)]

results = []
for x in Xi:
    for y in Yi:
        for z in Zi:
            if x + y + z != N:
                results.append([x,y,z])
print(results)
