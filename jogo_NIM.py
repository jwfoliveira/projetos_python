'''
Programa: Jogo do NIM em que a computador sempre vence
    Autor: José Wesley Feitosa Oliveira
    Concluída em: 11/2019
    Breve descricao:
    Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente, 
    retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
    Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
    O objetivo é criar um jogo em Python que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a 
    estratégia vencedora descrita acima.
    Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe 
    sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
    Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa"
    Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa"
    Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao 
    jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
'''

''' Função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à 
próxima jogada do computador de acordo com a estratégia vencedora. '''

def computador_escolhe_jogada(n,m): 

    aux = n%(m+1)
    jogada = peças_restantes =  0

    if aux == 0 or aux >= m:
        jogada = m
    else:
        jogada = aux

    peças_restantes = n - jogada
    print("Computador tirou",jogada,"peças")    
    print("Agora restam",peças_restantes,"peças no tabuleiro.\n")

    return jogada

''' Função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado 
é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma 
jogada válida. '''    

def usuario_escolhe_jogada(n,m):

    jogada = int(input("Quantas peças você vai tirar? "))
    peças_restantes = 0

    while jogada > m or jogada > n or jogada <= 0:
        print("Oops! Jogada inválida! Tente de novo. \n")
        jogada = int(input("Quantas peças você vai tirar? "))
    
    peças_restantes = n - jogada
    print("Voce tirou",jogada,"peças.")
    print("Agora restam",peças_restantes,"peças no tabuleiro. \n")
    return jogada

''' A função partida não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre 
jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da 
estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram 
removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" 
ou "Você ganhou!" conforme o caso. '''

def partida():
                 
    n_digitado = int(input("Quantas peças? "))
    m_digitado = int(input("Limite de peças por jogada? "))
    jogada = 0
    usuario_jogou =  True
    peças_restantes = 0

    while m_digitado >= n_digitado:
        n_digitado = int(input("Quantas peças? "))
        m_digitado = int(input("Limite de peças por jogada? "))

    if n_digitado%(m_digitado + 1) == 0:
        print("\n Voce começa! \n")
        jogada = usuario_escolhe_jogada(n_digitado,m_digitado)
        usuario_jogou =  True
    else:
        print("\n Computador começa! \n")
        jogada = computador_escolhe_jogada(n_digitado,m_digitado)
        usuario_jogou =  False
        
    n_digitado = n_digitado - jogada
    
    while n_digitado != 0:

        if usuario_jogou:
            jogada = computador_escolhe_jogada(n_digitado,m_digitado)            
            usuario_jogou =  False
        else:
            jogada = usuario_escolhe_jogada(n_digitado,m_digitado)
            usuario_jogou =  True

        n_digitado = n_digitado - jogada
        
    if usuario_jogou:
        print("\n Você ganhou! \n")
        return False
    else:
        print("\n O computador ganhou! \n")
        return True

''' A função campeonato realiza três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato '''

def campeonato():
    
    rodada1 = rodada2 = rodada3 = True
    voce = computador = 0
    
    print("\n **** Rodada 1 **** \n")
    rodada1 = partida()
    if rodada1:
        computador = 1
    else:
        voce = 1
    
    print("\n **** Rodada 2 **** \n")
    rodada2 =partida()
    if rodada2:
        computador = computador + 1
    else:
        voce = voce + 1
        
    print("\n **** Rodada 3 **** \n")
    rodada3 =partida()
    if rodada3:
        computador = computador + 1
    else:
        voce = voce + 1

    print("\n **** Final do campeonato! **** ")
    
    print("\n Placar: Você",voce,"X",computador," Computador")

    return


print("\n Bem-vindo ao jogo do NIM!  Escolha: ")
print("\n1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

tipo_jogo = int(input(" "))

while tipo_jogo != 1 and tipo_jogo != 2:
    print("\n1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    tipo_jogo = int(input(" "))
        
if tipo_jogo == 1:
    print("\n Você escolheu uma única partida ")
    partida()
else:
    print("\n Voce escolheu um campeonato! ")
    campeonato()

