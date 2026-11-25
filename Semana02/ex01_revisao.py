#  ex01_revisao.py
# Objetivo: Entender tipos (STR, int, float, bool) e a conversao com int()

# --- Experimentos de texto x numero (para treinar) ---
# print("3" + "1")
# print(3 + 1)
# print(int("3") + 1)
# print("3" * 3)
#  -Codigo para treinar variaveis.

# --- Dados do cliente ---
# cliente = "Marcos"
# valor_servico = 150.50
# quantidade_pecas = "3"
# pago = False

# # Aqui o int() converte só para a conta; A variavel continua str
# print (cliente, valor_servico, int(quantidade_pecas) + 1, pago)
# print(type(cliente), type(valor_servico), type(quantidade_pecas), type(pago)) #STR=TEXTO, INT=NUM.INT, FLOAT=NUM. C. Virg., BOOL=TRUE/FALSE/

# # Agora guardo o numero de volta na gaveta: ela passa a ser int
# quantidade_pecas = int(quantidade_pecas)
# print(type(quantidade_pecas))
# end

 ## DIA 12

# valor = float(input("Valor do serviço: "))

# if valor >= 100:
#     print("Serviço médio ou grande")
# else:
#     print("Serviço pequeno")

 ## DIA 13

# ex04_orcamento.py

# 1. PEDIR: serviço (float), quantidade de peças (int), valor de cada peça (float)

# 2. GUARDAR: total = serviço + quantidade * valor da peça

# 3. DECIDIR: se total >= 500, aplicar 10% de desconto; senão, sem desconto

# 4. MOSTRAR: o total final com 2 casas decimais, numa f-string

# servico = float(input("Valor do serviço: "))
# qtd_pecas = int(input("qtd_pecas: "))  
# valor_peca = float(input("valor_peca: "))

# total = servico + qtd_pecas * valor_peca


# if total >= 500:
#     desconto = total * 0.10
#     total = total - desconto

# print(f"Total: R$ {total:.2f}")

# Dia 14 - Refazendo exercícios anteriores para fixar

# Orçamento: calcula o total de um serviço e aplica desconto se necessário

# 1. Perguntar: valor da mão de obra, quantidade de peças e valor de cada peça
# 2. Calcular o total (mão de obra + quantidade vezes o valor da peça)
# 3. Se o total for 500 ou mais, aplicar 10% de desconto
# 4. Mostrar o total final com 2 casas decimais

# mao_de_obra = float(input("valor da mão de obra: "))
# qtd_pecas =  int(input("Quantidade de peças: "))
# valor_peca = float(input("Valor da peça: "))
# print(mao_de_obra, qtd_pecas, valor_peca)

# total = (mao_de_obra + qtd_pecas * valor_peca)

# if total >= 500:
#     desconto = total * 0.10
#     total = total - desconto
# print(f"total: R$ {total:.2f}")

## DIA - 15

# 1. Pedir: valor da conta e valor pago (os dois com centavos)
# 2. Decidir: o valor pago é maior ou igual ao da conta?
# 3. Se sim: calcular e mostrar o troco (pago menos conta)
# 4. Se não: calcular e mostrar quanto falta (conta menos pago)

# conta = float(input("Valor da conta: "))
# pago = float(input("Valor pago:  "))

# if pago >= conta:
#     troco = pago - conta
#     print(f"troco: R$ {troco:.2f}")


# else:
#     falta = conta - pago
#     print(f"Falta: R$ {falta:.2f}")

## DIA - 16

# 1. Pedir: Qual é o numero?
# 2. Decidir: Definir se o aquele numero é par ou impar!
# 3. Mostrar: par ou impar!

# numero = int(input("Difite um número inteiro: "))

# if numero % 2 == 0:
#     print("Par")
# else:
#     print("Impar")

## DIA - 17

# 1. Pedir: Quanto tempo demorou?
# 2. decidir: Isso foi rapido, normal ou demorou?
# 3. Mostrar: O tempo que levou.

# dias = int(input("Dias do reparo: "))

# # if dias <= 2:
# #     print("Expresso")

# # elif dias <= 7:
# #     print("Normal")

# # else:
# #     print("Demorado")

## DIA - 18

# 1. Pedir quantos dias o reparo levou.
# 2. Decidir em qual faixa os dias se encaixam:
#    até 2 dias: Expresso / até 7 dias: Normal / mais de 7: Demora.
# 3. Mostrar o prazo.

# dias = int(input("Dias do reparo: "))

# if dias <= 2:
#     print("Expresso")

# elif dias <=7: 
#     print("Normal")

# else:
#     print("Demorado")

## DIA 19 -

# 1. Pedir: as três notas
# 2. Calcular: a média (a soma das três notas dividida por 3)
# 3. Decidir em qual faixa a média cai:
#    7 ou mais: Aprovado / 5 ou mais: Recuperação / abaixo de 5: Reprovado
# 4. Mostrar: a média com 2 casas decimais e a situação

# nota1 = float(input("Nota 1: "))
# nota2 = float(input("Nota 2: "))
# nota3 = float(input("Nota 3: "))

# media = (nota1 + nota2 + nota3) / 3

# print(f"Média: {media:.2f}")

# if media >= 7:
#     print("Aprovado")
# elif media >= 5:
#     print("Recuperação")
# else:
#     print("Reprovado")

## DIA 20 -

# 1. Pedir: o valor da hora e a quantidade de horas trabalhadas
# 2. Calcular: o total (valor da hora vezes as horas)
# 3. Decidir: se as horas passarem de 5, somar R$ 50 de taxa extra ao total
# 4. Mostrar: o total em reais com 2 casas decimais

# valor_hora = float(input("Valor da hora: "))
# horas = float(input("Quantidade de horas: "))

# total = (horas * valor_hora)

# if horas > 5:
#     total = total + 50
# print(f"Total: R$ {total:.2f}")

# 1. Pedir: Valor por km e a distancia em km.
# 2. Calcular: o total (valor do km vezes o km)
# 3. Decidir: Se passar de 10 km soma 20,00 de taxa de deslocamento
# 4. Mostrar: o total em reais com 2 casas decimais


valor_km = float(input("Valor do KM rodado: "))
distancia = float(input("Quantidade de KM total: "))

total = distancia * valor_km

if distancia > 30: 
    total = total + 60

elif distancia > 10:
    total = total + 20


print(f"Total: R$ {total:.2f}")