

idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
horasSono = float(input('Quantas horas dormiu nas últimas 24h? '))

if idade>18 and idade<=69 and peso>=50 and horasSono>=6:
    print('Está apto para doar')
else:
    print('Não corresponde as necessidades mínimas.')
