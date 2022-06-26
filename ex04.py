#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 4 - Faça um programa que ao entrar um valor
# inteiro, seja impresso se correspondente binário.

# entrada de dados:
valor = int(input("Digite um número: ")) # Recebe o valor do número a ser calculado o binário

# processamento e saida de dados:
palavra = [] # Inicializa a lista que armazenará a palavra binária
for i in range(0, 8): # Loop que calcula o binário do número
    if valor % 2 == 0: # Se o resto da divisão do número atual por 2 for 0
        palavra.append("0") # Adiciona 0 na lista
        valor = valor // 2 # Divide o número atual por 2
    else: # Se o resto da divisão do número atual por 2 for diferente de 0
        palavra.append("1") # Adiciona 1 na lista
        valor = valor // 2 # Divide o número atual por 2
palavra.reverse() # Inverte a lista
print("O número binário é: ", end="") # Imprime o texto "O número binário é: " antes da lista
for i in palavra: # Loop que percorre a lista e imprime o binário do número
    print(i, end="") # Imprime o item atual da lista e não pula linha
print("") # Imprime uma quebra de linha após o binário
print("Fim do programa")


###################
print("----------------------------------------------------")
print(" outra forma é usar a função bin(valor)")
print("----------------------------------------------------")
# entrada de dados:
valor = int(input("Digite um número: ")) # Recebe o valor do número a ser calculado o binário
# processamento e saida de dados:
print("O número binário é: ", bin(valor)) # Imprime o binário do número
print("só o binário é: ", bin(valor)[2:]) # Imprime o binário do número, sem o 0b
print("Fim do programa")