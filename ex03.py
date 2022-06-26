#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 3 - Faça um algoritmo que imprima a quantidade
# de ocorrências para cada item contido em uma
# lista. Exemplo:   ['a', 'b', 'a', 'a', 'b', 'c', 'd', 'c', 'c', 'a', 'b', 'd', 'd', 'a', 'b']
#
# entrada de dados:
lista = ['a', 'b', 'a', 'a', 'b', 'c', 'd', 'c', 'c', 'a', 'b', 'd', 'd', 'a', 'b']
# processamento:
print("Lista: ", lista)
# fazer cast da lista para set para remover os valores repetidos
conjunto = set(lista) # Cria um conjunto com os elementos da lista (sem repetições)

# processamento e saida de dados:
for i in set(lista): # Loop que percorre o conjunto e imprime a quantidade de ocorrências de cada elemento
    contador = lista.count(i) # Conta a quantidade de ocorrências do elemento atual na lista (i)
    print(f"O item '{i}' aparece {contador} vezes") # Imprime a quantidade de ocorrências do elemento atual (i)

print("Fim do programa")



