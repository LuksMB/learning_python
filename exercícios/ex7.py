primeiro_nome = input("Digite seu primeiro nome: ")

if len(primeiro_nome) < 5:
    print(f'Seu nome é bem curto! Prazer, {primeiro_nome}.')

elif len(primeiro_nome) < 7:
    print(f'Belo nome, tamanho padrão, beleza natural! Prazer {primeiro_nome}.')

else:
    print(f'Que nome longo, adorei! Prazer {primeiro_nome}.')