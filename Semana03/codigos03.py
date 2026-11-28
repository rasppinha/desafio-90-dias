## Dia 22 - Inicio da terceira semana conforme o cronograma.

# total = 0
# for i in range(3):
#     valor = float(input("Valor da peça: "))
#     total = total + 50
# print(f"Total: R$ {total:.2f}")

## Dia 23 - Refazendo o exercio anterior de uma forma mais simplificada para ajudar a fixar.

  #Print 3 vezes para exemplificar oque o "for" faz sozinho sem repetir o codigo.

# print ("Olá")
# print ("Olá")
# print ("Olá")

  # O "for" vai fazer isso com um codigo só, pq se eu precisasse de "100x olá" não vou precisar de 100 linhas de codigo.

# for vez in range(3):
#     print("Olá")

 # O "for" vai mostrar 3 vezes o que esta na gaveta que é o "vez" porem o "range" inicia a contagem a partir do 0...

# for vez in range(3):
#     print(vez)

 # Mesmo codigo para contar a partir do 1, para isso no print eu adiciono + 1.

# for vez in range (3):
#     print(vez+1)

## Exemplo de como o recuo faz a diferença, o que esta dentro vai rodar o for 3 vezes que é o range(3), e depois vai rodar o print.

# for vez in range(3):
#     print("dentro")
# print("fora")

## com o recuo dentro do for, ele intercala os prints rodando ambos 3x.

# for vez in range(3):
#     print("dentro")
#     print("fora")

## Como o for funciona contando as "voltas"  gaveta total é 0, entao a cada "volta" ele conta ex: 1ª 0+10 = 10, 2ª 10+10=20... Se tirar o print do for o resultado vai ser 30 pois vai rodar e somar todas voltas e mostrar o print.

# total = 0
# for vez in range(3):
#     total = total + 10
#     print(total)

## Para treinar o print com buracos

# nome = "Marcos"
# total = 60
# print(f"{nome}, seu total: R$ {total:.1f}")

## Juntando os dois exercicios do dia:

# total = 0
# for peca in range(3):
#     valor = float(input("Valor da peça: "))
#     total = total + valor
# print(f"Total: R$ {total:.2f}")
-----------------------------------------