total_venda = float(input("Digite o total da venda: "))

# a. Total a pagar com desconto de 10%
total_com_desconto = total_venda * 0.9

# b. Valor de cada parcela no parcelamento de 3x sem juros
valor_parcela = total_venda / 3

# c. Comissão do vendedor na venda à vista (5% sobre o valor com desconto)
comissao_avista = total_com_desconto * 0.05

# d. Comissão do vendedor na venda parcelada (5% sobre o valor total)
comissao_parcelada = total_venda * 0.05

print(f"Total a pagar com desconto de 10%: R$ {total_com_desconto:.2f}")
print(f"Valor de cada parcela (3x sem juros): R$ {valor_parcela:.2f}")
print(f"Comissão do vendedor (venda à vista): R$ {comissao_avista:.2f}")
print(f"Comissão do vendedor (venda parcelada): R$ {comissao_parcelada:.2f}")