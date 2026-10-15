class Livro:
    def __init__(self, titulo, autor, ano, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__paginas = paginas
        
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_ano(self):
        return self.__ano
    
    def get_paginas(self):
        return self.__paginas
    
    def mostrar_informacoes(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Ano: {self.__ano}")
        print(f"Páginas: {self.__paginas}")

    def set_Titulo(self,novoTitulo):
        if novoTitulo:
            self.__titulo = novoTitulo
        else:
            print('Título NÃO pode ser VAZIO!')

    def set_paginas(self, qtd_paginas):
        if qtd_paginas <= 0:
            print("O livro/folheto precisa ter pelo menos 1 página!")
        else:
            self.__paginas = qtd_paginas

        if qtd_paginas <= 49:
            print("Folheto")
        else:
            print("Livro")
            
    def set_autor(self, novoAutor):
        if novoAutor:
            self.__autor = novoAutor
        else:
            print("Alguém escreveu está bomba, cade o autor???")
            

livro = Livro('Caso das 7 mulheres','Érico Veríssimo',1940, 300)
livro.mostrar_informacoes()
novoTitulo = "O Alienista"
novoAutor = "Machado de assis"
# # sendo PRIVADO Não ocorre erro, mas NÃO altera o VALOR
# livro.__titulo=novoTitulo
# livro.mostrar_informacoes()

livro.set_paginas(34)
livro.set_Titulo(novoTitulo)
livro.set_autor(novoAutor)
livro.mostrar_informacoes()