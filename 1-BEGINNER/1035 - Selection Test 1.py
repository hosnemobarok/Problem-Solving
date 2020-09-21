A,B,C,D = map(int, input().split())
if B>C and A<D and (C+D)>(A+B):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')