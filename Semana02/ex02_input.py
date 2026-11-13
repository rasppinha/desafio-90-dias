# exercicio, ex02_input.py
# Obejetivo: Receber dados do usario e mostrar numa frase.
nome = input("Nome do cliente: ") # Input devolve sempre o texto
valor = float(input("valor do serviço: ")) # Float converte o texto em número
print(f"Cliente {nome} deve r$ {valor:.2f}")