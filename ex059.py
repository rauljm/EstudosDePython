from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
alt = 0
while alt != 5:
    print('=-=' * 10)
    alt = int(input('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    >>>>> Qual é a sua opção? 
    '''))
    if alt == 1:
        print('O resultado da soma entre {} e {} = {}'.format(n1, n2, n1+n2))
    elif alt == 2:
        print('O resultado da multiplicação entre {} e {} = {}'.format(n1, n2, n1*n2))
    elif alt == 3:
        lista = [n1, n2]
        print('Entre {} e {} o maior número é {}'.format(n1, n2, max(lista)))
    elif alt == 4:
        n1 = int(input('Primeiro novo valor: '))
        n2 = int(input('Segundo novo valor: '))
    elif alt > 5:
        print('Alternativa inválida! Tente novamente.')
    else:
        print('Finalizando...')
    sleep(2)
print('FIM DO PROGRAMA. VOLTE SEMPRE!')
