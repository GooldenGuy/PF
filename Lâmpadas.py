#Lâmpadas
l1 = 0
l2 = 0

#Total de Apertos
total = int(input('Digite quantas vezes os interruptores serão alterados: '))

#Escolhendo os Interruptores
for x in range (1, total + 1):
    interruptor = int(input('\nDigite qual interruptor você ira alterar: '))
    if interruptor == 1:
        if l1 == 0:
            l1 = 1
        elif l1 == 1:
            l1 = 0

    elif interruptor == 2:
        if l1 == 0:
            l1 = 1
        elif l1 == 1:
            l1 = 0

        if l2 == 0:
            l2 = 1
        elif l2 == 1:
            l2 = 0
    else:
        print('Erro! Interruptor inexistente!')
        break

print(f'\nLâmpada1: {l1} | Lâmpada2: {l2}')