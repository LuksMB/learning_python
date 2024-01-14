# Funções Auxiliares
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a*b

def exponenciar(a, b):
    return a**b

def dividir(a, b):
    return a/b

# Principal
print(f'{5*"*"}Calculadora{5*"*"}\n')
while True:
    
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')

    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print('\nDigite apenas números! Reiniciando calculadora...\n')
        continue

    print('Operações disponíveis:\n(+) Adição\n(-) Subtração\n(*) Multiplicação\n(/) Divisão\n(**) Exponenciação\n')
    op = input('Digite a operação desejada: ')

    if op == '+':
        print(somar(num1, num2))
    elif op == '-':
        print(subtrair(num1, num2))
    elif op == '*':
        print(multiplicar(num1, num2))
    elif op == '**':
        print(exponenciar(num1, num2))
    elif op == '/':
        print(dividir(num1, num2))
    else:
        print('\nDigite uma das operações disponíveis usando o símbolo entre parênteses! Reiniciando calculadora...\n')
        continue

    resposta = input('Deseja encerrar?\nDigite (s) para sair ou qualquer tecla para continuar: ')
    
    if resposta.lower() == 's':
        break

print('\nEspero que tenha gostado!\n')