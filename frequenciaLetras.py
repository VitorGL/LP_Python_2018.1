lista = []

def frq(text):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    maior = 0
    maiores = ''

    for i in range(len(alfabeto)):
        if maior <= text.count(alfabeto[i]):
            if maior == text.count(alfabeto[i]):
                maiores = "{}{}".format(maiores, alfabeto[i])
                maior = text.count(alfabeto[i])
            else:
                maiores = alfabeto[i]
                maior = text.count(alfabeto[i])

    lista.append(maiores)

N = int(input())

for i in range(N):
    texto = input().lower()
    frq(texto)

for i in range(N):
    print('{}\n'.format(lista[i]))