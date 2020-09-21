#not Accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1065

positivos = []
negativos = []

for v in range(1, 6):
    valor = int((input()))
    if valor % 2 == 0:
        if valor > 0:
            positivos.append(valor)

        elif valor < 0:
            if valor % 2 == 0:
                positivos.append(valor)


print('%d valores pares'%(len(positivos)))
