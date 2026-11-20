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

numero = int(input("Difite um número inteiro: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")