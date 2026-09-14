from P06_3487_pilha_encadeada import PilhaEncadeada as PE
class FilaEncadeada:
    def __init__(self):
        self.pilha_de_entrada=PE()
        self.pilha_de_saida=PE()
        self.tamanho=0
    def __len__(self):
        return self.tamanho
    def enfileirar(self, item):
        self.pilha_de_entrada.push(item)
        self.tamanho+=1
    def desenfileirar(self):
        if len(self.pilha_de_saida)==0 and len(self.pilha_de_entrada)==0:
            raise IndexError ("A fila está vazia")
        if len(self.pilha_de_saida)==0:
         while not self.pilha_de_entrada.esta_vazia():
            self.pilha_de_saida.push(self.pilha_de_entrada.pop())
        self.tamanho-=1
        return self.pilha_de_saida.pop()
        
    def frente(self):
        if len(self.pilha_de_saida)==0 and len(self.pilha_de_entrada)==0:
            raise IndexError ("A fila está vazia")
        if len(self.pilha_de_saida)==0:
            while not self.pilha_de_entrada.esta_vazia():
             self.pilha_de_saida.push(self.pilha_de_entrada.pop())
        return self.pilha_de_saida.topo()
    def esta_vazia(self):
        return True if len(self)==0 else False
    def __repr__(self):
        if self.esta_vazia():
         return "Fila vazia"
        j=[]
        while not self.pilha_de_saida.esta_vazia():
            j.append((self.pilha_de_saida.pop()))
        k=[]
        while not self.pilha_de_entrada.esta_vazia():
            k.append((self.pilha_de_entrada.pop()))
        l=j+list(reversed(k))
        for i in range(len(l)):
            self.pilha_de_saida.push(l[len(l)-i-1])

        return " > ".join(list(map(str, l)))



        
a=FilaEncadeada()
a.enfileirar(1)
a.enfileirar("ovni")
a.enfileirar("Pão")
print(a)

