import os

palavra_secreta = "excalibur"
descoberta_atual = "*********"
num_letras = len(palavra_secreta)
contador_tentativas = 0
print(f'Jogo da adivinhação -- A palavra possui {num_letras} letras. Boa sorte!')
while True:
    letra = input("Digite uma letra: ")
    if (len(letra) == 1) and letra.isalpha:
        letra = letra.lower()
    else:
        print("Digite uma e somente uma letra!")
        continue
    
    contador_tentativas += 1

    pos_carac = 0
    for caractere in palavra_secreta:
        for char in descoberta_atual:
            if caractere == letra:
                lista = list(descoberta_atual)
                lista[pos_carac] = caractere
                nova_string = "".join(lista)
                descoberta_atual = nova_string
                break
        pos_carac += 1

    print(f'Texto descoberto: {descoberta_atual}')
    if(palavra_secreta == descoberta_atual):
        break

os.system('cls')
print(f'Você venceu após {contador_tentativas} tentativas. Parabéns!')
print(f'A palavra secreta era {palavra_secreta}.')