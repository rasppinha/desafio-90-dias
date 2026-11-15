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

 ## DIA 11

# valor = float(input("Valor do serviço: "))

# if valor >= 100:
#     print("Serviço médio ou grande")
# else:
#     print("Serviço pequeno")

 ## DIA 12

# ex04_orcamento.py

# 1. PEDIR: serviço (float), quantidade de peças (int), valor de cada peça (float)

# 2. GUARDAR: total = serviço + quantidade * valor da peça

# 3. DECIDIR: se total >= 500, aplicar 10% de desconto; senão, sem desconto

# 4. MOSTRAR: o total final com 2 casas decimais, numa f-string

servico = float(input("Valor do serviço: "))
qtd_pecas = float(input("qtd_pecas"))  
valor_peca = float(input("valor_peca"))
print(servico, qtd_pecas, valor_peca)

total = (servico + qtd_pecas * valor_peca)
print(total)