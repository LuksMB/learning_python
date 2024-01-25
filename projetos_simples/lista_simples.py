import os #os.system('cls')

#Início da seção de funções

def inserir(l):
    valor = input('Digite o item da lista a ser inserido: ')
    l.append(valor)

def apagar(l):
    if len(l) == 0:
        print('A lista atualmente está vazia, não existem itens para apagar\n')
    else:
        indice = input("Digite a posição do item que deseja remover: ")
        try:
            indice = int(indice)
            valor = l[indice]
            l.pop(indice)
            print(f'Item "{valor}" removido com sucesso!\n')
        except:
            print('Posição inválida. Nenhum item foi apagado\n')

def listar(l):
    if len(l) == 0:
        print('**Lista vazia**\n')
        return

    print('**Lista**')
    for indice, valor in enumerate(l):
        print(indice, valor)
    print('')

#Fim da seção de funções

lista = []
while True:
    selecao = input('Selecione uma opção\n[i]nserir\n[a]pagar\n[l]istar\n[s]air\nescolha: ')
    
    os.system('cls')

    if selecao == 's':
        break
    elif selecao == 'i':
        inserir(lista)
    elif selecao == 'a':
        apagar(lista)
    elif selecao == 'l':
        listar(lista)
    else:
        print("Nenhuma das opções oferecidas foi selecionada, tente novamente")

print('A lista foi encerrada, volte sempre!')