nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

space = 'Sim' if " " in nome else "Não"

if idade and nome:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém espaços? {space}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios')