import random


def boas_vindas(idioma):
    if idioma == 1:
        print('Seja bem vindo ao jogo de acertar o número aleatorio!\nAs regras são as seguintes:')
        print('Você tem que acertar o número que estou pensando, de 1 a 100')
        print('Você pode escolher seu número de tentativas selecionando a dificuldade')
        print('----------------------------------------------------------------------')
    elif idioma == 2:
        print('Welcome to the game of matching the random number!\nThe rules are as follows:')
        print('You have to match the number Im thinking of, from 1 to 100')
        print('You can choose your number of attempts by selecting the difficulty')
        print('----------------------------------------------------------------------')


def resposta(x, tentativas, idioma):
    numero_aleatorio = random.randint(1, x)
    if idioma == 1:
        print(f'Você tem {tentativas} tentativa(s) para acertar.')
    elif idioma == 2:
        print(f'You have {tentativas} attempt(s) to guess.')

    while tentativas > 0:
        try:
            if idioma == 1:
                entrada = int(input(f'Coloque um numero de 1 {x}: '))
            elif idioma == 2:
                entrada = int(input(f'Enter a number between 1 and {x}: '))

            if entrada < 1 or entrada > x:
                if idioma == 1:
                    print(f'Coloque um numero entre 1 a {x}')
                elif idioma == 2:
                    print(f'Enter a number between 1 to {x}')
                continue
        except ValueError:
            if idioma == 1:
                print('Valor inexistente')
            elif idioma == 2:
                print('Non-existent value')
            continue

        if entrada > numero_aleatorio:
            if idioma == 1:
                print('Número muito alto!')
            elif idioma == 2:
                print('Very high number! try a lower one ')
        elif entrada < numero_aleatorio:
            if idioma == 1:
                print('Número muito baixo! Tente um mais alto')
            elif idioma == 2:
                print('Very low number! Try a higher one')
        else:
            if idioma == 1:
                print(f'Correto! O número era {numero_aleatorio}')
            elif idioma == 2:
                print(f'Correct! The number was {numero_aleatorio}')
            return

        tentativas -= 1
        if idioma == 1:
            print(f'Você ainda tem {tentativas} tentativa(s) restante(s)')
        elif idioma == 2:
            print(f'You still have {tentativas} remaining attempt(s)')

    if idioma == 1:
        print(f"Você perdeu! Suas tentativas acabaram, a resposta era {numero_aleatorio}")
    elif idioma == 2:
        print(f'You lost! Your attempts are over, the answer was {numero_aleatorio}')


def escolher_idioma():
    print('Escolha seu idioma / Choose your language')
    print('1: Português / Portuguese')
    print('2: English')

    while True:
        try:
            idioma = int(input("Digite o número correspondente / Enter the number: "))
            if idioma == 1:
                return idioma
            elif idioma == 2:
                return idioma
            else:
                print("Opção inválida. Tente novamente / Invalid option. Please try again.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número / Invalid input. Please enter a number.")


def selecionar_dificuldade(idioma):
    if idioma == 1:
        dificuldade = {
            1:  (': Fácil (10 tentativas)', 10),
            2:  (': Médio (5 tentativas)', 5),
            3:  (': Difícil (3 tentativas)', 3)
        }
    elif idioma == 2:
        dificuldade = {
            1: (': Easy (10 attempts)', 10),
            2: (': Medium (5 attempts)', 5),
            3: (': Hard (3 attempts)', 3)
        }

    while True:
        opcoes = list(dificuldade.keys())
        opcoes.sort()
        for entry in opcoes:
            print(entry, dificuldade[entry][0])
        try:
            if idioma == 1:
                escolha = int(input('Selecione a dificuldade: '))
            elif idioma == 2:
                escolha = int(input('Select difficulty: '))
            if escolha in dificuldade:
                _, tentativas = dificuldade[escolha]
                return tentativas
            else:
                if idioma == 1:
                    print('Opção inexistente')
                elif idioma == 2:
                    print('Non-existent option')
        except ValueError:
            print('Non-existent value')


idioma = escolher_idioma()
boas_vindas(idioma)

tentativas = selecionar_dificuldade(idioma)
resposta(100, tentativas, idioma)
