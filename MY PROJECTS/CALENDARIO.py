import calendar

print('GERADOR DE CALENDARIO')

mes = int(input('Digite o numero do mês (1-12): '))
ano = int(input('Digite o ano: '))

if mes < 1 or mes > 12:
    print('Mês invalido! Digite um numero entre 1 e 12. ')

else:
    print('\n SEU CALENDARIO:\n')
    print(calendar.month(ano, mes))
