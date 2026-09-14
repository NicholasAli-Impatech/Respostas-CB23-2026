class node:
    def __init__(self, item, anterior=None):
        self.dado = item
        self.anterior = anterior
class lista_encadeada:
    def __init__(self):
        self.head=None
        self.tamanho=0

class PilhaEncadeada(lista_encadeada):

    def __len__(self):
        return self.tamanho
        
  
    def push(self, item):
        novo_no=node(item)
        self.head, novo_no.anterior=novo_no, self.head
        self.tamanho+=1
    
    def pop(self):
        if self.head==None:
            raise IndexError ("Pilha vazia")
        a=self.head.dado
        self.head=self.head.anterior
        self.tamanho-=1
        return a
    def topo(self):
        if self.head==None:
            raise IndexError ("Pilha vazia")
        return self.head.dado
    def esta_vazia(self):
        return self.head is None
    
    def __repr__(self):
        atual=self.head
        if atual==None:
            return ""
        else:
            x=[]
            while atual.anterior is not None:
                x.append(str(atual.dado))
                atual=atual.anterior
            x.append(str(atual.dado))
            return " > ".join(x)





        

        
