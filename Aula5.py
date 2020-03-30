def lista_de_argumentos (**dicionario):
    print (dicionario)

lista_de_argumentos (a= 1, b= 2, c= 3, d= 4)

print ()
def estudo ():
    print ("Estamos estudando as funções")

estudo ()

print ()
def verificaString (palindromo):
    if palindromo == palindromo[::-1]:
        print ("É um palíndromo!")
    else:
        print ("Não é um palíndromo")

verificaString ("arara")

print ()
def funcao ():
    def subFuncao ():
        x= 20
        print (x)
        return x

    subFuncao ()
funcao ()
