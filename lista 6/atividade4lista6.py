'''4 – Crie uma classe chamada Produto com:
• Atributos: nome e quantidade.
• Um método chamado esta_disponivel que retorna True se a quantidade for maior
que 0 e False caso contrário.
• Um método chamado vender que diminui a quantidade em 1.
Teste criando um objeto, verificando a disponibilidade, vendendo produtos e verificando
novamente.'''

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        
    def esta_disponivel(self):
        if self.quantidade>0:
            i = True
        else:
            i = False
        return i
        
    def vender(self):
        self.quantidade = self.quantidade-1
        return f"A quantidade atual é {self.quantidade}"
        
n = input("Nome: ")
q = int(input("Quantidade: "))

produto1  = Produto(n, q)
if produto1.esta_disponivel():
    print ("está")
else:
    print ("não está")
print (produto1.vender())
if produto1.esta_disponivel():
    print ("está")
else:
    print ("não está")