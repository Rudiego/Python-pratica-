'''
como achar o fatorial de um número
'''
numero = int(input("insira o numero: "))

fatorial = 1

if numero < 0:
    print("não existe fatorial de numeros negativos")
elif numero == 0:
    print(f"Fatorial de {numero} eh 1 ")
else:
    for x in range (1,numero + 1):
        fatorial = fatorial*x
    print(f'O fatorial de {numero} eh: {fatorial}')
