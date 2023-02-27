'''
01 - Implemente um programa que receba a 
idade de uma pessoa e imprima mensagem de
acordo com os critérios:
'''
'''idade = input("qual a idade? ")

if float(idade) < 16:
    print("Menor")
elif int(idade) >= 16 and int(idade) == 18:
    print('EMANCIPADO')
elif float(idade) > 18:
    print('MAIOR')

print("saindo do programa...")'''

'''
02 - Implemente um programa que receba a idade de um 
nadador e imprima a sua
categoria seguindo as regras:
Infantil A = 5-7 anos
Infantil B = 8-10 anos
Juvenil A = 11-13 anos
Juvenil B = 14-17 anos 
'''
idade = input("insira a sua idade: ")
print("Direcionando você...")

if int(idade) >= 5 and int(idade) <= 7:
    print("Infantil A")
elif int(idade) >= 8 and int(idade) <= 10:
    print("Infantil B")
elif int(idade) >= 11 and int(idade) <= 13:
    print("Juvenil A")
elif int(idade) >= 14 and int(idade) <= 17:
    print('Juvenil B')
elif int(idade):
    print("Idade não bate com nossas opções, favor contatar nossa central")
print("Finalizando seleção...")
