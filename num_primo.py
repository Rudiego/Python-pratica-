'''
Descubra se o numero é primo 
'''

print(30 * "-")

numero = int(input("insira um numero para descobrir se o mesmo eh primo: "))

if numero > 1:
    for x in range(2,numero):
        if (numero % x) == 0:
            print("Esse não eh um primo")
            break
    else:
        print("Esse numero eh primo")
else:
    print("esse numero não eh primo -> numero - ou = a 1 ")

print(30 * "-")