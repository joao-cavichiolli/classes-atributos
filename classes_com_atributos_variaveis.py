## Iremos declarar uma variavel nos atributos do construtor da classe

class Livro():

    def __init__(self,titulo,autor,editora):
        self.titulo = titulo 
        self.autor = autor
        self.editora =  editora

    def imprime(self):
        print("Esse livro é %s e o Autor %s"%(self.titulo,self.autor))


### Instanciando os Objetos

livro1 = Livro("Titulo do Livro 1","Titulo1","Ed1") # esse possui 1 namespace ou self

livro2 = Livro("Titulo do Livro 2","Autor do Livro2","ED2") # Esse possui outro 
#namespace ou valor self de valores de atributos diferente

print(livro1.titulo)
print(livro1.editora)
print(livro2.autor)

livro1.imprime()
livro2.imprime()

print(livro1.editora)


