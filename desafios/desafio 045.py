import random

n1 = ('Pedra')
n2 = ('papel')
n3 = ('tesoura')

lista = [n1, n2, n3]
computador = random.choice(lista)

print('''[ 1 ] Pedra
[ 2 ] Papel 
[ 3 ] Tesoura ''')
jogador = int(input('Qual a sua jogada? '))

if computador == n1 and jogador == 2:
    print('Você venceu')
