a = 11
b = 8
c = 2

if b > a: 
    print("b eh maior que a")

#ou

if b > a: print("b eh maior que a")
print("codigo fora do bloco")

print("B") if b > a else print("A")

if a > b:
    print("A")
    if a > c:
        print("A maior q C")