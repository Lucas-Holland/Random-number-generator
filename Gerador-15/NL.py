from random import randint
lotofacil = []
numeros = [1, 25]
count = c = 0
for c in range(0, 100):
    while len(lotofacil) < 15:
        if count < 1:
            escolha = randint(numeros[0], numeros[1])
            lotofacil.append(escolha)
        else:
            while escolha in lotofacil:
                escolha = randint(numeros[0], numeros[1])
            lotofacil.append(escolha)

        count+=1
lotofacil.sort()
print(len(lotofacil))
print(f"Os números sorteados foram:")
for c in range(0,15):
    print(f"\033[34m{lotofacil[c]}\033[m", end=' | ')
