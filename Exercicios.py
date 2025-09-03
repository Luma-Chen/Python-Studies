import random

def evenNumber():
    numero = int(input("Digite um número inteiro: "))
    if (numero % 2 == 0):
        print("É um número par!")
    else:
        print("É um número ímpar!")

def calcIMC():
    peso= float(input("Digite seu peso: "))
    altura= float(input("Dgite sua altura: "))
    imc= peso/(pow(altura, 2))
    if (imc < 18.5):
        print("Você está abaixo do peso")
    elif (imc >= 18.5 and imc < 25):
        print("Você está no peso ideal")
    elif (imc >= 25 and imc < 30):
        print("Você está com sobrepeso")
    else:
        print("Você está obeso")

def resulGrade():
    nota1= float(input("Digite sua nota 1: "))
    nota2= float(input("Digite sua nota 2: "))
    nota3= float(input("Digite sua nota 3: "))
    media= (nota1 + nota2 + nota3)/3
    if (media >= 6):
        print("Aprovado(a)!")
    else:
        print("Reprovado(a)")

def guessNumber():
    numero = random.randint(1, 100)
    x= 1
    while True:
        palpite= int(input("Digite um número inteiro de 1 a 100: "))
        if (palpite == numero):
            print("Você acertou o número! Levou %d tentativas" % (x))
            break
        elif (palpite < numero):
            print("Tente um número maior na próxima vez.")
        else:
            print("Tente um número menor na próxima vez.")
        x+= 1

evenNumber()
calcIMC()
resulGrade()
guessNumber()