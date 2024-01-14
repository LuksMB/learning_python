horas = input("Com licença, que horas são?\n")
hora = horas[0] + horas[1]

try:
    hora = int(hora)
    if hora <= 11 and hora >= 0:
        print('Obrigado, tenha um bom dia!')
    elif hora <= 17 and hora >= 12:
        print('Obrigado, tenha um boa tarde!')
    else:
        print('Obrigado, tenha uma ótima noite!')

except:
    print("Não entendi, sinto muito pelo incômodo.")