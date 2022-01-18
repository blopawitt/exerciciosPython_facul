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

#Nesse exercício eu cometi um erro e recebi o feedback do professor:
#"Ex3: não valida o 1 como número de Fibonacci, teste se código sempre com os valores extremos"
#Para corrigir esse problema eu troquei o valor da variavel a para 0 e assim a troca de variaveis acontece corretamente e o valor 1 é incluso.



