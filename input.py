'''
sistema utilizadando input()
'''

print("Insira seu nome: ")
nome = input()
print("Olá, "+nome)

idade = input("Qual a sua idade? ")
print("certo, "+idade, "anos")

print("seu nome eh: {0} e Sua idade eh: {1}".format(nome, idade))

nome = input("Qual seu nome? ")
idade = input("Qual a sua idade? ")

print(f'seu nome eh: {nome} e sua idade eh: {idade}')
