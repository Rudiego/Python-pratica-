'''
teste de conhecimento em exercicios

1 - área de um Retangulo
2 - área de um quadrado
3 - Se o produto que você quer avaliar custa (??) reais,
qual sera o desconto do mesmo com (??)%
4 - área do círculo
5 - conversão de reias para dolar
6 - conversão de dolar para reias
'''

'#(1)Área do Retangulo'


# base = input("insira a base desejada para o retangulo: ")
# altura = input("insira a altura desejada para o retangulo: ")
# area = float(base) * float(altura)

# print(f'area calculada:{area} m')

'''
caso ocorra problemas ou você queria verificar
o tipo de cada item sempre lembrar de usar 'type'
print(type(base))
'''


'''
Exercicio 2

lado = input("Digite o tamanho do lado do quadro: ") # Obetendo metrica

area = int(lado) * int(lado)

print(area)
'''

"""
Exercicio 3


Preço = input("Digite o Preço do produto: ")
Desconto = input("Digite o Desconto a ser aplicado: %")

apdesconto = float(Preço) * float(Desconto) / 100

print("Desconto de: R$", int(apdesconto))
"""

"""
Exercicio 4

Raio = input("Digite o raio do: ")
Pi = 3.14
calculo = (int(Raio) * int(Raio)) * Pi

print(calculo)"""


"""
exercicio 5
"""

'''print("Olá Bem vindo ao sistema de transferencia de cambio")

real = input("Digite a quantia que sera trocada: ")

conta = int(real) / 5.07

print('Valor convertido para dolar: $',conta)'''

# Sistema Basico de escolha de moeda

print("bem vindo ao serviço")
moeda = input("selecione a moeda desejada [real = 1 / dolar = 2 / euro = 3]:")
if int(moeda) == 1:
    print("Real selecionado")
    real = input("selecionar cambio [dolar = 1 / euro = 2]")

    if int(real) == 1:
        print("Selecionando moeda...")
        print("Dolar selecionado")
        real1 = input("selecionar quantia para transação: ")
        real_dolar = int(real1) / 5.06
        print(f"total transferido {real1}... total de cambio {real_dolar}")
    elif int(real) == 2:
        print("Selecionando moeda...")
        print("Euro selecionado")
        real2 = input("Selecionar quantia para transação: ")
        real_euro = int(real2) / 0.82
        print(f"total transferido {real2}... total de cambio {real_euro}")

elif int(moeda) == 2:
    print('Dolar escolhido')
    dolar = input("Selecionar ['real = 1 / euro = 2']")

    if int(dolar) == 1:
        print("moeda selecionada...")
        print("Real selecionado")
        dolar1 = input("Selecionar quantia para transação: ")
        dolar_real = int(dolar1) * 5.06
        print(f'Total transferido {dolar1}... total de cambio {dolar_real}')
    elif int(dolar) == 2:
        print("moeda selecionada...")
        print("Euro selecionado")
        dolar2 = input("Selecionar quantia para transação: ")
        dolar_euro = int(dolar2) * 0.92
        print(f'Total transferido {dolar2}... total de cambio {dolar_euro}')


elif int(moeda) == 3:
    print("Moeda selecionada")
    print("Euro selecionado")
    euro = input("Selecionar ['real = 1 / dolar = 2']")

    if int(euro) == 1:
        print("moeda selecionada...")
        print("Real selecionado")
        euro1 = input("Selecionar quantia para transação: ")
        euro_real = int(euro1) * 5.50
        print(f'Total transferido {euro1}... total de cambio {euro_real}')
    elif int(euro) == 2:
        print("moeda selecionada...")
        print("Euro selecionado")
        dolar2 = input("Selecionar quantia para transação: ")
        euro_dolar = int(dolar2) * 0.91
        print(f'Total transferido {dolar2}... total de cambio {euro_dolar}')
else:
    print('identação não encontrada... reiniciando sistema...')
    print("aguarde...")
    print("Erro de Sistema tente novamente...")
