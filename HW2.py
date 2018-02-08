import numpy as np
import matplotlib.pyplot as plt
import random
import time

# Cria o tabuleiro e iniciliza todas as posições com zero
def create_board():
    return np.zeros((3,3))

# Realiza uma jogada
def place(board, player, position):
    board[position] = player

# Lista as opções disponiveis para a realização de uma jogada
def possibilities(board):
    (x,y) = np.where(board==0)
    return list(zip(x, y))

# Realiza uma jogada randomica
def random_place(board, player):
    selection = possibilities(board)
    s = random.choice(selection)
    place(board, player, s)

# verifica se o jogador fechou uma linha
def row_win(board, player):
    return np.any(np.all(board==player,axis=1))

# verifica se o jogador fechou uma coluna
def col_win(board, player):
    return np.any(np.all(board==player,axis=0))

# verifica se o jogador fechou as 2 diagonais
def diag_win(board, player):
    return np.all(board.diagonal()==player) or np.all(np.fliplr(board).diagonal()==player)

# verifica se existe algum ganhador
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board,player) or col_win(board,player) or diag_win(board,player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# Inicia uma partida
def play_game():

    board, winner = create_board(), 0

    while winner == 0:
        for player in [1,2]:
            random_place(board,player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

# Inicia uma partida pela posição (1,1)
def strategy_play_game():

    board, winner = create_board(), 0

    board[(1,1)] = 1

    while winner == 0:
        for player in [1,2]:
            random_place(board,player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

# Tempo inicial do processamento
start = time.time()

# Realiza 1000 jogos 
result = [play_game() for i in range(1000)]

# Tempo final
stop = time.time()

# Tempo final do processamento
print(stop-start)

# Plot o gráfico
plt.hist(result, bins = np.linspace(-2, 4, 24) )
plt.show()
