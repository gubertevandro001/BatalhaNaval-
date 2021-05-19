import random

tabuleiro = []
pontos = 0
cpu_pontos = 0
lista = [] #Lista criada para armazenar os posicionamentos de barcos do humano
listapc = [] #Lista criada para armazenar os posiciomanetos de barcos do pc

for i in range(0, 10):
    posicoes = []
    for j in range(0, 10):
        posicoes.append('X')
    tabuleiro.append(posicoes)


def mostrar_tabuleiro(): #Tabuleiro ficou extenso, pois não consegui fazer ele ficar elegante e do jeito certo com um código menor.
    print('\033[34m================= Batalha Naval =================\033[m\n')
    print(f'\033[1;97mSeus Pontos: {pontos}\033[m')
    print(f'\033[1;97mPontos do Computador: {cpu_pontos}\033[m\n')
    print('\033[1;33m    0    1    2    3    4    5    6    7    8    9\033[m')
    print('\033[1;33m 0 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[0]):
        print(f'\033[31m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 1 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[1]):
        print(f'\033[31m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 2 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[2]):
        print(f'\033[31m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 3 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[3]):
        print(f'\033[31m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 4 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[4]):
        print(f'\033[31m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 5 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[5]):
        print(f'\033[35m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 6 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[6]):
        print(f'\033[35m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 7 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[7]):
        print(f'\033[35m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 8 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[8]):
        print(f'\033[35m {linha}   ', end='\033[m')
    print()
    print('\033[1;33m 9 ', end='\033[m')
    for i, linha in enumerate(tabuleiro[9]):
        print(f'\033[35m {linha}   ', end='\033[m')
    print()


def humano_jogadas(): #Fiz várias repetições, indicando casos de erro no momento de informar a posição dos barcos
    for p in range(0, 5):
        while True:
            try: #Tratamento de exceção para validar se o jogador joga uma letra ou outro caractere ao invés de um número
                humano_linha = int(input(f'\n\033[;1mInforme a Linha Onde Deseja Posicionar seu {p + 1}º Barco: \033[m'))
                while humano_linha < 0 or humano_linha > 4:
                    print('\033[1;97mEste é o Campo Adversário, ou Esse Campo Nem Existe! Informe Linhas de 0 a 4.\033[m')
                    humano_linha = int(input(f'\n\033[;1mInforme a Linha Onde Deseja Posicionar seu {p + 1}º Barco: \033[m'))
                else:
                    humano_coluna = int(input('\033[;1mAgora Informe a Coluna Desejada, Respeitando a Linha Escolhida: \033[m'))
                    while humano_coluna < 0 or humano_coluna > 9:
                        print('\033[1;97mColunas Só Vão Até 9! Tente Novamente.\033[m')
                        humano_coluna = int(input('\033[;1mAgora Informe a Coluna Desejada, Respeitando a Linha Escolhida: \033[m'))
                    else:
                        tabuleiro[humano_linha][humano_coluna] = '\033[97m╧\033[m'
                        mostrar_tabuleiro()
                        while [humano_linha, humano_coluna] in lista: #Caso a posição informada já tenha sido preenchida gera um erro e não adiciona a jogada na lista.
                            print('\033[1;97mPosição Ocupada! Tente Novamente.\033[m')
                            humano_linha = int(input(f'\033[;1mInforme a Linha Onde Deseja Posicionar Seu {p + 1}º Barco: \033[m'))
                            while humano_linha < 0 or humano_linha > 4:
                                print('\033[1;97mEste é o Campo Adversário, ou Esse Campo Nem Existe! Informe Linhas de 0 a 4.\033[m')
                                humano_linha = int(input(f'\033[;1mInforme a Linha Onde Deseja Posicionar Seu {p + 1}º Barco: \033[m'))
                            else:
                                humano_coluna = int(
                                input('\033[;1mAgora Informe a Coluna Desejada, Respeitando a Linha Escolhida: \033[m'))
                                while humano_coluna < 0 or humano_coluna > 9:
                                    print('\033[1;97mColunas Só Vão Até 9! Tente Novamente.\033[m')
                                    humano_coluna = int(
                                    input('\033[;1mAgora Informe a Coluna Desejada, Respeitando a Linha Escolhida: \033[m'))
                                else:
                                    tabuleiro[humano_linha][humano_coluna] = '\033[97m╧\033[m'
                                    mostrar_tabuleiro()
                        else:
                            lista.append([humano_linha, humano_coluna]) #Caso posição ainda não ocupada, adiciona na lista
                            break
            except ValueError:
                print('\033[1;97mDigite Somente Números! Tente Novamente\033[m')


def cpu_jogadas():
    for c in range(0, 5):
        cpu_linha = random.randint(5, 9)
        cpu_coluna = random.randint(0, 9)
        tabuleiro[cpu_linha][cpu_coluna] = '\033[35mX\033[m'
        while [cpu_linha, cpu_coluna] in listapc: #Caso o pc gere uma posição ja ocupada por ele mesmo, ele gera novamente até ser uma posição que esteja livre
            cpu_linha = random.randint(5, 9)
            cpu_coluna = random.randint(0, 9)
            tabuleiro[cpu_linha][cpu_coluna] = '\033[35mX\033[m'
        else:
            listapc.append([cpu_linha, cpu_coluna]) #Caso posição ainda não ocupada, adiciona na listapc
    print('\033[1;96m   OS BARCOS DO SEU ADVERSÁRIO ESTÃO OCULTOS!\033[m\n')


def mensagem_inicio_ataques():
    print('\033[1;97m   =======Iniciando Rodada de Ataques=======\033[m\n')


def ataques(tabuleiro): #Também realizei várias repetições indicando erros na hora dos ataques
    lista_ataques_cpu = []#Lista para armazenar os ataques do pc
    lista_ataques_humano = [] #Lista para armazenas os ataques do humano
    while True:
        try:
            humano_ataque_linha = int(input('\033[;1mInforme a Linha Que Deseja Atacar: \033[m'))
            while humano_ataque_linha < 5 or humano_ataque_linha > 9:
                print('\033[1;97mVocê Não Pode Atacar o Seu Próprio Campo, Nem Atacar um Campo Que Não Existe. Ataque o Campo do Seu Adversário!\033[m')
                humano_ataque_linha = int(input('\033[;1mInforme a Linha Que Deseja Atacar: \033[m'))
            else:
                humano_ataque_coluna = int(input('\033[;1mInforme a Coluna Que Deseja Atacar: \033[m'))
                while humano_ataque_coluna < 0 or humano_ataque_coluna > 9:
                    print('\033[1;97mColunas Vão Somente Até 9! Escolha Corretamente!\033[m')
                    humano_ataque_coluna = int(input('\033[;1mInforme a Coluna Que Deseja Atacar: \033[m'))
                else:
                    while [humano_ataque_linha, humano_ataque_coluna] in lista_ataques_humano: #Caso a posição informada já esteja ocupada ou errada ele não adiciona na lista e volta a pedir
                        print('\033[1;97mPosição Já Atacada! Tente Novamente.\033[m')
                        humano_ataque_linha = int(input('\033[;1mInforme a Linha Que Deseja Atacar: \033[m'))
                        while humano_ataque_linha < 5 or humano_ataque_linha > 9:
                            print('\033[1;97mVocê Não Pode Atacar o Seu Próprio Campo, Nem Atacar um Campo Que Não Existe. Ataque o Campo do Seu Adversário!\033[m')
                            humano_ataque_linha = int(input('\033[;1mInforme a Linha Que Deseja Atacar: \033[m'))
                        else:
                            humano_ataque_coluna = int(input('\033[;1mInforme a Coluna Que Deseja Atacar: \033[m'))
                            while humano_ataque_coluna < 0 or humano_ataque_coluna > 9:
                                print('\033[1;97mColunas Vão Somente Até 9! Escolha Corretamente!\033[m')
                                humano_ataque_coluna = int(input('\033[;1mInforme a Coluna Que Deseja Atacar: \033[m'))
                    else:
                        lista_ataques_humano.append([humano_ataque_linha, humano_ataque_coluna]) #Guarda os ataques do humano caso não repetido
                        tabuleiro[humano_ataque_linha][humano_ataque_coluna] = '\033[92m*\033[m'
                        mostrar_tabuleiro()

                    if [humano_ataque_linha, humano_ataque_coluna] in listapc: #Verifica na lista_pc se a posição informada corresponde a um barco do computador, caso seja, afunda o barco do pc
                        tabuleiro[humano_ataque_linha][humano_ataque_coluna] = '\033[92m⚓\033[0m'
                        global pontos
                        pontos += 1
                        mostrar_tabuleiro()
                        print(f'\033[1;34m{"-" * 42}\nParabéns Você Afundou um Navio Adversário!\n{"-" * 42}\n\033[m')
                        if pontos == 5:
                            print('\033[1;34mPARABÉNS HUMANO, VOCÊ VENCEU O COMPUTADOR!!!\033[m')
                            break
                    else:
                        tabuleiro[humano_ataque_linha][humano_ataque_coluna] = '\033[92m*\033[m' #Caso posição informada não corresponda a nenhum barco do pc, o humano erra o tiro
                        print('\033[1;93m------------------\nVocê Errou o Tiro!\n------------------\033[m')

            cpu_ataque_linha = random.randint(0, 4)
            cpu_ataque_coluna = random.randint(0, 9)
            while [cpu_ataque_linha,
                cpu_ataque_coluna] in lista_ataques_cpu:  # Verifica se a jogada do computador já está ocupada ou repetida, caso esteja, ele gera novamente
                cpu_ataque_linha = random.randint(0, 4)
                cpu_ataque_coluna = random.randint(0, 9)
            else:
                lista_ataques_cpu.append(
                [cpu_ataque_linha, cpu_ataque_coluna])  # Guarda os ataques do pc caso não repetido
            if [cpu_ataque_linha, cpu_ataque_coluna] in lista:  # Verifica na lista se a posição corresponde a um barco do humano, caso seja, afunda o barco dele
                tabuleiro[cpu_ataque_linha][cpu_ataque_coluna] = '\033[93m⚓\033[0m'
                global cpu_pontos
                cpu_pontos += 1
                mostrar_tabuleiro()
                print(f'\033[1;37m{"-" * 31}\nUm de Seus Navios Foi Afundado!\033[m\n{"-" * 31}')
                if cpu_pontos == 5:
                    print('\033[1;34mO COMPUTADOR VENCEU!!!\033[m')
                    break
            else:
                tabuleiro[cpu_ataque_linha][
                cpu_ataque_coluna] = '\033[93m*\033[m'  # Caso posição informada não corresponda a nenhum barco do humano, o pc erra o tiro
                mostrar_tabuleiro()
                print('\033[1;37m--------------------\nO PC Errou o Tiro!\n--------------------\033[m')
        except ValueError:
            print('\033[1;97mInforme Somente Números! Tente Novamente\033[m')


mostrar_tabuleiro()
humano_jogadas()
cpu_jogadas()
mensagem_inicio_ataques()
ataques(tabuleiro)

