a = 1
b = 1
c = 0
n = int(input("Digite um número inteiro: "))
while c < n:
    c = a + b
    b = a
    a = c
if c == n:
    print("Ação bem sucedida!")
else:
    print("A ação falhou.")




