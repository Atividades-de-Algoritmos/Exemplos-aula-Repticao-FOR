#
#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 08/06/2022
#
# 3 - Faça um algoritmo que imprima a quantidade
# de ocorrências para cada item contido em uma
# lista. Exemplo: ['a', 'b', 'a', 'a', 'b', 'c', 'd', 'c', 'c', 'a', 'b', 'd', 'd', 'a', 'b']
#

# Entrada de dados

lista = ['a', 'b', 'a', 'a', 'b', 'c', 'd', 'c', 'c', 'a', 'b', 'd', 'd', 'a', 'b'] # Lista com diversas strings

# Processamento e saída de dados

print(f"Lista: {lista}\n") # Imprimindo a lista completa

conjunto = set(lista) # Utilizando o set() para transformar a lista em um conjunto eliminando todas as repetições

for i in conjunto: # Loop que percorre o conjunto e imprime a quantidade de ocorrências de cada elemento
    contador = lista.count(i) # Conta a quantidade de ocorrências do elemento atual na lista (i)
    print(f"O item '{i}' aparece {contador} vezes") # Imprime a quantidade de ocorrências do elemento atual (i)

print("\nfim do programa") # Informando ao usuário que o programa terminou
