# Cria o tabuleiro do jogo
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Exibe o tabuleiro na tela
def exibir_tabuleiro():
    print(tabuleiro[0][0] + "|" + tabuleiro[0][1] + "|" + tabuleiro[0][2])
    print("-+-+-")
    print(tabuleiro[1][0] + "|" + tabuleiro[1][1] + "|" + tabuleiro[1][2])
    print("-+-+-")
    print(tabuleiro[2][0] + "|" + tabuleiro[2][1] + "|" + tabuleiro[2][2])

# Permite que o jogador faça uma jogada
def fazer_jogada(linha, coluna, jogador):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False

# Verifica se houve um vencedor ou empate
def verificar_vencedor():
    # Verifica linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return tabuleiro[i][0]
    # Verifica colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return tabuleiro[0][i]
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]
    # Verifica empate
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return None
    return "Empate"