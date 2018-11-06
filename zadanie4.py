from random import randint
import sys


def komunikat(typ):
    print('+------------------+')
    if typ == 'g':
        print('+Gracz wygrywa !   +')
    elif typ == 'k':
        print('+Komputer wygrywa !+')
    else:
        print('+Remis !           +')
    print('+------------------+')


things = ['P', 'K', 'N']
opisy = {'P': 'Papier', 'K': 'Kamień', 'N': 'Nożyce'}
punktacja = {'Gracz': 0, 'Komputer': 0}

while True:
    gracz = (input("Wybierz figurę: (P)apier , (K)amień , (N)ożyce >")).upper()

    if gracz not in 'PKN':
        continue

    print('Gracz: {}'.format(opisy[gracz]))

    komp = things[randint(0, 2)]
    print('Komputer: {}'.format(opisy[komp]))

    if gracz == 'P' and komp == 'K':
        punktacja['Gracz'] += 1
        komunikat('g')
    elif gracz == 'K' and komp == 'N':
        punktacja['Gracz'] += 1
        komunikat('g')
    elif gracz == 'N' and komp == 'P':
        punktacja['Gracz'] += 1
        komunikat('g')
    elif gracz == komp:
        punktacja['Gracz'] += 1
        punktacja['Komputer'] += 1
        komunikat('r')
    else:
        punktacja['Komputer'] += 1
        komunikat('k')

    print("Aktualny wynik: Gracz {}:{} Komputer".format(punktacja['Gracz'], punktacja['Komputer']))

    while True:
        question = (input("Gramy dalej [t/n]? >")).lower()
        if question == 't':
            break
        elif question == 'n':
            print('Dzięki za grę !')
            sys.exit()
