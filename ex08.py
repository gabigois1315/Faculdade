# questao 8 lista 3
#idade da pessoa 30 anos
# dias= 30* 365 ( 30 seria a idade e 365 dias e um ano) = 10950
#quantas horas ele viveu= 24*10950= ( 24 é hr em um dia e 10950 dias vividos) = 262800
# entradas= idade (int)
#saidas= dias e horas (int)
#sempre resolver o problema em papel para depois passar pro codigo

idade = int(input('informe a idade do usuario:'))

dias_vividos= 365 * idade
horas_vividas = 24 * dias_vividos

print(f'Dias vividos {dias_vividos}')
print(f'Horas vividos {horas_vividas}')
