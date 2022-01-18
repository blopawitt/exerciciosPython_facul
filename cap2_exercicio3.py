seg = int(input("Quantos votos para segunda-feira: "))
ter = int(input("Quantos votos para terça-feira: "))
qua = int(input("Quantos votos para quarta-feira:"))
qui = int(input("Quantos votos para quinta-feira: "))
sex = int(input("Quantos votos para sexta-feira: "))

if seg > ter and seg > qua and seg > qui and seg > sex:
    print("Segunda-feira foi o dia escolhido!")
elif ter > seg and ter > qua and ter > qui and ter > sex:
    print("Terça-feira foi o dia escolhido!")
elif qua > seg and qua > ter and qua > qui and qua > sex:
    print("Quarta-feira foi o dia escolhido!")
elif qui > seg and qui > ter and qui > qua and qui > sex:
    print("Quinta-feira foi o dia escolhido!")
elif sex > seg and sex > ter and sex > qua and sex > qui:
    print("Sexta-feira foi o dia escolhido!")
else:
    print("Empate, fazer nova votação.")