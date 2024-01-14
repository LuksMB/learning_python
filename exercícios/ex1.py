nome = 'Lucas'
sobrenome = 'Braga'
ano_nascimento = 2002
idade = 2023 - ano_nascimento
maioridade = 'Sim' if idade >= 18 else 'Não'
altura_metros = 1.76

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maioridade)
print('Altura em metros:', altura_metros, end='m')