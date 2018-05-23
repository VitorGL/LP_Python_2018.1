#n = int(input())
#b = int(input())
n,b = map(int,input().split())

def criaMatriz(n, matriz):
    for i in range(1, n+1):
        linha = []
        for j in range(1,n+1):
            linha.append(1)
        matriz.append(linha)

def imprimeMatriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end=' ')
        print("\n")


matriz = []
criaMatriz(n, matriz)
nL = 0
nT = 0
nR = n-1
nB = n-1
k = 0
t = True
x = 0
y = 0

while k <= b and t == True:

    if t == True:
        for i in range(nL,nR+1):
            if k == b:
                x = nT+1
                y = i
                t = False
                break
            matriz[nT][i] = 0
            k+=1
        
    nT+=1

    if t == True:
        for i in range(nT,nB+1):
            if k == b:
                x = i
                y = nR+1
                t = False
                break
            matriz[i][nR] = 0
            k+=1

    nR-=1

    if t == True:
        for i in range(nR,nL-1,-1):
            if k == b:
                x = nB+1
                y = i+2
                t = False
                break
            matriz[nB][i] = 0
            k+=1

    nB-=1

    if t == True:
        for i in range(nB,nT-1,-1):
            if k == b:
                x = i+2
                y = nL+1
                t = False
                break
            matriz[i][nL] = 0
            k+=1

    nL+=1
        
#imprimeMatriz(matriz)
#print("(",x,",",y,")")
print(x,y)
