with open('exercícios/utilizados/texto_exemplo.txt', 'r', encoding='utf-8') as arquivo:
    frase = arquivo.read().lower()

    repetiu_mais = frase[0]
    num_repeticoes_max = 1
    i = 0
    j = 0
    contador_temp = 0

    while i < len(frase):
        if frase[i] != ' ':
            while j < len(frase):
                if frase[i] == frase[j]:
                    contador_temp += 1
                j += 1
            if contador_temp > num_repeticoes_max:
                num_repeticoes_max = contador_temp
                repetiu_mais = frase[i]
        contador_temp = 0
        i += 1
    
    print(f'O caractere mais repetido nessa frase, foi o "{repetiu_mais}", que repetiu-se por {num_repeticoes_max} vezes.')
