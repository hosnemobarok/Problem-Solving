#Dimikoj accept

T = int(input())
for i in range(1, T+1):
    X = float(input())
    count = 0
    while(X > 1.0):
        X = X / 2
        count += 1
    print(count,'days')
