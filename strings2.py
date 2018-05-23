
def subs(a, b):
    aux = 0
    maior = 0
    
    for i in range(0,len(b)):
        for j in range(1,len(b)+1):
            if a.find(b[i:j]) >= 0:
                aux = j - i
                if maior < aux: maior = aux
                
    print(maior)

        
a = input()
b = input()
subs(a, b)
