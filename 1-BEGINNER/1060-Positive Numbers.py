#accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1060

positivos = []
negativos = []

for v in range(1, 7):
      valor = float(input())

      if valor > 0:
            positivos.append(valor)
            continue

      '''else:
            negativos.append(valor)
            continue
      '''

qnt = len(positivos)
print('%d valores positivos'%qnt)