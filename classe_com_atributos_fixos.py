### O metodo construtor __init__ ele
# COnstroi os atributos para uma instancia

## o self ou também chamada de namespace
# São os valores atribuidos e exclusivos para cada
# atributo de um objeto

## Metodo e uma ação que podemos configurar dentro de uma classe
# Pode atuar com o objeto ou não.

class Livro():
    def __init__(self):
        self.titulo = "Curso de Python"
        self.autor = "Guido Van Rossum"
    
    # Uma funcao dentro de classe vira método
    def imprime(self):
        print("Esse Livro é %s e o Autor %s"%(self.titulo,self.autor))


## Instanciar os objetos

livro1 =Livro()

print(livro1)

## Listar os atributos do objecto

print(livro1.titulo)
print(livro1.autor)

livro1.imprime()


livro2 = Livro()

livro2.imprime()
