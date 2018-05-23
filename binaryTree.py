class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self._inserir(valor, self.raiz)

    def _inserir(self, valor, node):
        if valor < node.valor:
            if (node.esqr != None):
                self._inserir(valor, node.esqr)
                node.esqr.mae = node
            else:
                node.esqr = No(valor)
        else:
            if node.dir != None:
                self._inserir(valor, node.dir)
                node.dir.mae = node
            else:
                node.dir = No(valor)

    def search(self, valor):
        if valor == self.valor:
            return self

        elif (self.dir == None) and (self.esqr == None):
            return

        elif self.valor > valor:
            self.esqr.search(valor)
        else:
            self.dir.search(valor)

    def emOrdem(self):
        if self.raiz != None:
            self.emOrdem_(self.raiz)
    def emOrdem_(self, node):
        if (node.esqr != None):
            self.emOrdem_(node.esqr)
        print(node.valor, end=" ")
        if (node.dir != None):
            self.emOrdem_(node.dir)

    def pre(self):
        if self.raiz != None:
            self.pre_(self.raiz)
    def pre_(self, node):
        print(node.valor, end=" ")
        if (node.esqr != None):
            self.pre_(node.esqr)
        if (node.dir != None):
            self.pre_(node.dir)

    def pos(self):
        if self.raiz != None:
            self.pos_(self.raiz)
    def pos_(self, node):
        if (node.esqr != None):
            self.pos_(node.esqr)
        if (node.dir != None):
            self.pos_(node.dir)
        print(node.valor, end=" ")

class No:
    def __init__(self, valor):
        self.valor = valor
        self.mae = None
        self.dir = None
        self.esqr = None


def executar():
    arvores = []

    C = int(input("Digite a quantidade de testes: "))
    # C = int(input())

    for caso in range(C):
        arvores.append(Arvore())

        N = int(input("Digite a quantidade de números: "))

        valores = input("valores: ")
        valores = valores.split()
        
        for n in range(N):
            arvores[caso].inserir(int(valores[n]))

    for caso in range(C):
        print("Case {}:".format(caso+1))
        print("Pre.:", end=" ")
        arvores[caso].pre()
        print()

        print("In.:", end=" ")
        arvores[caso].emOrdem()
        print()

        print("Post.:", end=" ")
        arvores[caso].pos()
        print("\n")





executar()
