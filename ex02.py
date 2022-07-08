#
# Autores:
# Michel Silva
# Carlos Eduardo
# data: 08/06/2022
#
# 2 – Faça programa que calcule o fatorial de um
# número.
#

# Entrada de dados

valor = int(input("Digite um número: ")) # Solicita o valor do número a ser calculado o fatorial

# Processamento de dados

fatorial = 1 # Inicializa o fatorial com 1
for i in range(1, valor + 1): # Loop que calcula o fatorial do número
    fatorial = fatorial * i # Multiplica o fatorial pelo número atual

# Saida de dados

print(f"O fatorial de {valor} é: {fatorial}") # Imprime o fatorial do número

print("\nfim do programa") # Informamos ao user que o programa terminou

# Versão 2.0 do código 

# -------------------------------------------------------------- #

# By: Carlos Eduardo

# number = int(input('Digite um número: ')) # Solicita um valor inteiro do user

# fatorial = 1 # Em fatorial o último valor sempre será 1 então defini como ponto de parada do loop

# for i in range(number, fatorial, -1): # Para cada item no tamanho de um número qualquer até o último elemento que é o 1 ande retroscendo, ou seja, se eu informar 10 como número ele de partida o item de sequência será 9, 8, 7, 6, 5, 4, 3, 2 
#     fatorial *= i # Fazendo a multiplação dos números e sendo acumulado na variável fatorial

# print(f'Fatorial de {number}: {fatorial}') # Imprimindo o valor do fatorial acumulado

# print('fim do programa') # Informando ao usuário que o programa terminou

# -------------------------------------------------------------- #