total_importancia = 780000.00

primeiro_ganhador_porcentagem = 0.46
segundo_ganhador_porcentagem = 0.32

primeiro_ganhador_valor = total_importancia * primeiro_ganhador_porcentagem
segundo_ganhador_valor = total_importancia * segundo_ganhador_porcentagem
terceiro_ganhador_valor = total_importancia - (primeiro_ganhador_valor + segundo_ganhador_valor)

print(f"Valor do primeiro ganhador: R$ {primeiro_ganhador_valor:.2f}")
print(f"Valor do segundo ganhador: R$ {segundo_ganhador_valor:.2f}")
print(f"Valor do terceiro ganhador: R$ {terceiro_ganhador_valor:.2f}")
