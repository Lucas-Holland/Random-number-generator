from random import randint
lotofacil= []
numb = []
lista = []
loto = []
maior = []
numeros = [1, 25]
c=p= 0

for c in range(0, 100000):
    esc = randint(numeros[0], numeros[1])
    loto.append(esc)

for c in range(1, 26):
    x = loto.count(c)
    numb.append(c)#número relacionado
    numb.append(x)#quantidade
    lista.append(numb[:])#adiciona os dois a lista
    numb.clear()

i = 0
while i <= 24:
    maior.append(lista[i][1])
    i += 1
maior.sort(reverse=True)

print("os 15 numeros que mais cairam foram:")
while len(lotofacil) <= 15:
    for p in range(len(lista)):
        if maior[0] == lista[p][1]:
            lotofacil.append(lista[p])
            maior.remove(maior[0])
lotofacil.sort()
for a in range(0, 15):
    print(f"{lotofacil[a][0]} > {lotofacil[a][1]}",end=' | ')


