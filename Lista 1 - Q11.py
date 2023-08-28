taxa_visita = 80.00
taxa_diaria = 55.00

dias_trabalho = int(input("Digite a quantidade de dias de trabalho: "))

total = taxa_visita + (taxa_diaria * dias_trabalho)

print(f"O encanador receberá um total de R$ {total:.2f}")