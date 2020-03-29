arquivo = open("entrada-labirinto-2.txt", "r")
todas_linhas_arquivo = arquivo.readlines()
arquivo.close()

matriz = {}
caminho = []
opcoes = {}

contador = 0
for linha in todas_linhas_arquivo:
    new_linha = []
    old_linha = linha.strip().split()
    for item in old_linha:
        if item == 'X':
            new_linha.append(item)
        elif item == '1':
            new_linha.append('P')
        else:
            new_linha.append(int(item))

    new_linha.insert(0, '')
    matriz[contador] = new_linha

    if 'X' in new_linha:
        caminho.append(['O', contador, new_linha.index('X')])
        matriz[contador][new_linha.index('X')] = 2

    contador += 1

tamanho_matriz = [matriz[0][1], matriz[0][2]]
del matriz[0]


def moverCima(L, C):
    if isinstance(matriz[L - 1][C], int):
        return matriz[L - 1][C]
    else:
        return 'N'


def moverBaixo(L, C):
    if isinstance(matriz[L + 1][C], int):
        return matriz[L + 1][C]
    else:
        return 'N'


def moverDireita(L, C):
    if isinstance(matriz[L][C + 1], int):
        return matriz[L][C + 1]
    else:
        return 'N'


def moverEsquerda(L, C):
    if isinstance(matriz[L][C - 1], int):
        return matriz[L][C - 1]
    else:
        return 'N'

voltar = -1
def decideMovimento():
    global voltar
    s = sorted(opcoes.values())
    if 0 in s:
        voltar = -1
        for k, v in opcoes.items():
            if v == s[0]:
                return k
                break
    else:
        ultimo = caminho[voltar][0]
        voltar -= 1
        if ultimo == 'C':
            return 'B'
        elif ultimo == 'E':
            return 'D'
        elif ultimo == 'D':
            return 'E'
        elif ultimo == 'B':
            return 'C'

def checkFim(L, C):
    if (L == tamanho_matriz[0] or C == tamanho_matriz[1]) and isinstance(matriz[L][C], int):
        return True
    else:
        return False


fim = False

while not checkFim(caminho[-1][1], caminho[-1][2]):

    C = moverCima(caminho[-1][1], caminho[-1][2])
    E = moverEsquerda(caminho[-1][1], caminho[-1][2])
    D = moverDireita(caminho[-1][1], caminho[-1][2])
    B = moverBaixo(caminho[-1][1], caminho[-1][2])
    semsaida = 0

    if isinstance(C, int):
        opcoes['C'] = C
    else:
        semsaida += 1

    if isinstance(E, int):
        opcoes['E'] = E
    else:
        semsaida += 1

    if isinstance(D, int):
        opcoes['D'] = D
    else:
        semsaida += 1

    if isinstance(B, int):
        opcoes['B'] = B
    else:
        semsaida += 1

    if semsaida == 3:
        matriz[caminho[-1][1]][caminho[-1][2]] = 'S'

    direcao = decideMovimento()
    if direcao == 'C':
        matriz[caminho[-1][1] - 1][caminho[-1][2]] += 1
        caminho.append(['C', caminho[-1][1] - 1, caminho[-1][2]])
    elif direcao == 'E':
        matriz[caminho[-1][1]][caminho[-1][2] - 1] += 1
        caminho.append(['E', caminho[-1][1], caminho[-1][2] - 1])
    elif direcao == 'D':
        matriz[caminho[-1][1]][caminho[-1][2] + 1] += 1
        caminho.append(['D', caminho[-1][1], caminho[-1][2] + 1])
    elif direcao == 'B':
        matriz[caminho[-1][1] + 1][caminho[-1][2]] += 1
        caminho.append(['B', caminho[-1][1] + 1, caminho[-1][2]])

    decideMovimento()
    opcoes.clear()

print(caminho)
