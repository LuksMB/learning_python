nome = input('Digite seu nome: ')
simbolo = input('Digite um caractere separador: ')

local = 0
nova_string = simbolo
while local < len(nome):
    nova_string += nome[local] + simbolo
    local += 1

print(nova_string)