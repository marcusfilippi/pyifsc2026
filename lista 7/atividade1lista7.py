'''1 - Livro e MarcadorDePagina (0..1).
Objetivo: Implementar um relacionamento opcional simples.
Classes: MarcadorDePagina e Livro.
Regras:
• A classe MarcadorDePagina deve ter um atributo pagina_atual.
• A classe Livro deve ter um atributo titulo e um total_paginas.
• Um Livro pode ter zero ou um MarcadorDePagina (ele começa sem marcador,
0..1).
• Crie um método no Livro chamado adicionar_marcador(pagina). Este método deve
criar uma instância de MarcadorDePagina e associá-la ao livro. Se o livro já tiver
um marcador, apenas atualize a pagina_atual dele.
Comprove o funcionamento da sua implementação no programa principal.
Veja, na figura abaixo, o Diagrama de Classes completo:'''

class MarcadorDePagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual
        
    def __repr__(self):
        return f"A página atual é {self.pagina_atual}"
        
class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.marcador = None
        
    def __repr__(self):
        return f"Titulo: {self.titulo}. Páginas: {self.total_paginas}"
        
    def adicionar_marcador(self, pagina_atual):
        if self.marcador:
            if pagina_atual<= self.total_paginas and pagina_atual>=0:
             self.marcador.pagina_atual = pagina_atual
        else:
            if pagina_atual<= self.total_paginas and pagina_atual>=0:
             self.marcador = MarcadorDePagina(pagina_atual)
            
t = input("Digite o titulo do seu livro: ")
tp = int(input("Digite o total de páginas do livro: "))
livro = Livro(t, tp)
print(livro)

# primeiro teste
if livro.marcador:
    print(livro.marcador)
else:
    print ("O livro não tem marcador")
    
#segundo teste
i = int(input("Digite a página atual que vocẽ está no seu livro: "))
livro.adicionar_marcador(i)

if livro.marcador:
    print(livro.marcador)
else:
    print ("O livro não tem marcador")
    
#terceiro teste
            
i = int(input("Digite a página atual que você está no seu livro: "))
livro.adicionar_marcador(i)

if livro.marcador:
    print(livro.marcador)
else:
    print ("O livro não tem marcador")
            
    
        
        