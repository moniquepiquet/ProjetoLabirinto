from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', '4', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]


def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")


def movimento(posicao: tuple, direcao: list):
    nova_posicao = [(posicao[0] + direcao[0]), (posicao[1] + direcao[1])]
    return nova_posicao
    

def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    #verifica se a posição para onde vai tem parede. Se tiver, retorna False. Caminho livre retorna True
    if LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == 'S':
        return True

    elif LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == ' ':
        return True
    else:
        return False

def main():
    POSICAO_INICIAL = [4, 5]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL
    historico = [] #pilha que armazena os movimentos
    preso = False
    while POSICAO_ATUAL != [9,18]:
        if not preso:
            if len(historico) == 0:
                POSICAO_ANTERIOR = []
                POSICAO_ATUAL = POSICAO_INICIAL
            preso = True
            if verifica_movimento(POSICAO_ATUAL, CIMA):
                POSICAO_ANTERIOR = POSICAO_ATUAL
                LABIRINTO[POSICAO_ANTERIOR[0]][POSICAO_ANTERIOR[1]] = '2'
                historico.append(POSICAO_ANTERIOR)
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
                LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
                preso = False
                print_labirinto()
                sleep(1)
            elif verifica_movimento(POSICAO_ATUAL, DIREITA):
                POSICAO_ANTERIOR = POSICAO_ATUAL
                LABIRINTO[POSICAO_ANTERIOR[0]][POSICAO_ANTERIOR[1]] = '2'
                historico.append(POSICAO_ANTERIOR)
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
                LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
                preso = False
                print_labirinto()
                sleep(1)
            elif verifica_movimento(POSICAO_ATUAL, BAIXO):
                POSICAO_ANTERIOR = POSICAO_ATUAL
                LABIRINTO[POSICAO_ANTERIOR[0]][POSICAO_ANTERIOR[1]] = '2'
                historico.append(POSICAO_ANTERIOR)
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
                LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
                preso = False
                print_labirinto()
                sleep(1)
            elif verifica_movimento(POSICAO_ATUAL, ESQUERDA):
                POSICAO_ANTERIOR = POSICAO_ATUAL
                LABIRINTO[POSICAO_ANTERIOR[0]][POSICAO_ANTERIOR[1]] = '2'
                historico.append(POSICAO_ANTERIOR)
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, ESQUERDA)
                LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
                preso = False
                print_labirinto()
                sleep(1)
        else:
            LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = '2'
            POSICAO_ATUAL = historico[-1]
            historico.pop()
            preso = False
    print("\nSucesso\n")



if __name__ == "__main__":
    main()
