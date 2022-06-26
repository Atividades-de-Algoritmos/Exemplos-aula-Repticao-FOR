#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 2 – Faça programa que calcule o fatorial de um
# número.
#
# entrada de dados:
valor = int(input("Digite um número: ")) # Recebe o valor do número a ser calculado o fatorial

# processamento:
fatorial = 1 # Inicializa o fatorial com 1
for i in range(1, valor + 1): # Loop que calcula o fatorial do número
    fatorial = fatorial * i # Multiplica o fatorial pelo número atual

# saida de dados:
print(f"O fatorial de {valor} é: {fatorial}") # Imprime o fatorial do número
#
print("Fim do programa")