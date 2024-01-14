numero = input('Digite um número inteiro: ')

try:
    print('Par' if int(numero) % 2 is 0 else 'Ímpar')
except:
    print('Não é um número inteiro')