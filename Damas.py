def linha(x):
    print('_'*x)


def apresentacao(matriz):

    for i in range(len(matriz)):
        linha(35)
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='')
        print()


matriz = [[' C / L ', '   1   ', '   2   ', '   3   ', '   4   ', '|'],
          ['   1   ', '|     |', '|  O  |', '|     |', '|  O  |', '|'],
          ['   2   ', '|     |', '|     |', '|     |', '|     |', '|'],
          ['   3   ', '|     |', '|     |', '|     |', '|     |', '|'],
          ['   4   ', '|  O  |', '|     |', '|  O  |', '|     |', '|']]

apresentacao(matriz)
linha(60)

while True:
    # Escolhendo a peça
    peca_escolhida = input('Escolha uma peça para movimentar ou digite "sair" para encerrar o jogo:').split()
    peca_escolhida[0] = peca_escolhida[0].lower()

    if peca_escolhida[0] == 'sair':
        break

    coluna_peca_escolhida, linha_peca_escolhida = int(peca_escolhida[0]), int(peca_escolhida[1])

    # Escolhendo a nova posição da peça
    nova_posicao = input('Escolha uma nova posição para a peça escolhida:').split()

    coluna_nova_posicao, linha_nova_posicao = int(nova_posicao[0]), int(nova_posicao[1])

    # MOVENDO AS PEÇAS
    matriz[coluna_nova_posicao].pop(linha_nova_posicao)
    print('1 passo:')
    apresentacao(matriz)

    matriz[coluna_nova_posicao].insert(linha_nova_posicao, matriz[linha_peca_escolhida][coluna_peca_escolhida])
    print('2 passo:')
    apresentacao(matriz)

    matriz[coluna_peca_escolhida].pop(linha_peca_escolhida)
    print('3 passo:')
    apresentacao(matriz)

    matriz[coluna_peca_escolhida].insert(linha_peca_escolhida, matriz[linha_nova_posicao][coluna_nova_posicao])
    print('4 passo:')
    apresentacao(matriz)