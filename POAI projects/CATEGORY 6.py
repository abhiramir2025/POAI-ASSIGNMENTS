#CATEGORY 6
# MIN-MAX SEARCH ALGORITHM - CHESS GAME

def minimax(depth, node_index, maximizing_player, values, max_depth):

    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, values, max_depth)
        )

    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, values, max_depth)
        )


# Sample evaluation values of chess positions
values = [3, 5, 2, 9, 12, 5, 23, 23]

max_depth = 3

best_score = minimax(
    0,
    0,
    True,
    values,
    max_depth
)

print("Best evaluation score for Chess:", best_score)


# ALPHA-BETA PRUNING ALGORITHM - CHESS GAME

def alpha_beta(depth, node_index, maximizing_player,
               values, max_depth, alpha, beta):

    if depth == max_depth:
        return values[node_index]

    if maximizing_player:

        best = float('-inf')

        for i in range(2):

            value = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                False,
                values,
                max_depth,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:

        best = float('inf')

        for i in range(2):

            value = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                True,
                values,
                max_depth,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Sample evaluation values of chess positions
values = [3, 5, 2, 9, 12, 5, 23, 23]

max_depth = 3

best_score = alpha_beta(
    0,
    0,
    True,
    values,
    max_depth,
    float('-inf'),
    float('inf')
)

print("Best evaluation score for Chess:", best_score)


# MIN-MAX SEARCH ALGORITHM - TIC-TAC-TOE

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
    print()


def check_winner(board):

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(board, maximizing):

    result = check_winner(board)

    if result == "X":
        return 1

    if result == "O":
        return -1

    if result == "Draw":
        return 0

    if maximizing:

        best_score = float('-inf')

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:

        best_score = float('inf')

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def find_best_move(board):

    best_score = float('-inf')
    best_move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "X"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


board = [
    "X", "O", "X",
    " ", "O", " ",
    " ", " ", " "
]

print("Current Board:")
print_board(board)

move = find_best_move(board)

print("Best move for X:", move + 1)

board[move] = "X"

print("\nBoard after Min-Max move:")
print_board(board)