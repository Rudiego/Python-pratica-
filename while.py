"""
while 
do while
"""

a = 1

while a <= 5:
    print(a)
    print( a <= 5)
    if a == 3:
        break
    a = a + 1
    print( a <= 5)

print("resultado final de A: ", a)