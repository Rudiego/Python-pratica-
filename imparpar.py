'''
Como descobrir se um número é impar ou par
'''

numero = int(input("Insira um numero para saber se o mesmo eh par: "))
if (numero % 2) == 0:
    print(f'{numero} eh par')
else:
    print(f'{numero} eh impar')