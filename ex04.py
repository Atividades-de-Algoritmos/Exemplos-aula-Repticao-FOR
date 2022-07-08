#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 04/07/2022
#
# 4 - Faça um programa que ao entrar um valor
# inteiro, seja impresso se correspondente binário.

# Entrada de dados

valor = int(input("Digite um número em decimal: ")) # Recebe o valor do número a ser calculado o binário

# Processamento e saída de dados

palavra = [] # Inicializa a lista que armazenará a palavra binária

while True: # Loop que calcula o binário do número
    
    if valor > 0: # Se o valor for maior que 0 vai buscar pelo binário, agora quando for negativo irá quebrar o código
        
        if valor % 2 == 0: # Se o resto da divisão do número atual por 2 for 0
            palavra.append("0") # Adiciona 0 na lista
            valor = valor // 2 # Divide o número atual por 2
        
        else: # Se o resto da divisão do número atual por 2 for diferente de 0
            palavra.append("1") # Adiciona 1 na lista
            valor = valor // 2 # Divide o número atual por 2
    else:
        break

palavra.reverse() # Inverte a lista

print("\nO número binário é: ", end="") # Imprime o texto "O número binário é: " antes da lista

for i in palavra: # Loop que percorre a lista e imprime o binário do número
    print(i, end="") # Imprime o item atual da lista e não pula linha
print() # Imprime uma quebra de linha após o binário

print("\nfim do programa") # Informando ao usuário que o programa terminou

# Versão 2.0 do código

# ------------------------------------------------------------------------- #

# print("----------------------------------------------------")
# print(" outra forma é usar a função built-in bin(valor)")
# print("----------------------------------------------------")

# Entrada de dados

# valor = int(input("Digite um número: ")) # Recebe o valor do número a ser calculado o binário

# Processamento e saida de dados

# print("O número binário é: ", bin(valor)) # Imprime o binário do número
# print("Só o binário é: ", bin(valor)[2:]) # Imprime o binário do número, sem o 0b
# print("Fim do programa") # Informando ao usuário que o programa terminou

# ------------------------------------------------------------------------- #