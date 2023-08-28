valor_produto = float(input("Digite o valor do produto: "))
desconto = 0.12

valor_com_desconto = valor_produto - (valor_produto * desconto)

print(f"O valor com desconto de 12% é: R$ {valor_com_desconto:.2f}")