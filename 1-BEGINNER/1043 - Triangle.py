#accept
A,B,C = map(float, input().split())
soma = (A + B + C)
area = (((A + B) * C) / 2)
if (A < B + C and B < A + C) and C < A + B:
    print ('Perimetro = %.1f' % soma)
else:
    print ('Area = %.1f' % area)