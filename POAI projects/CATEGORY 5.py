#CATEGORY 5
# GREEDY BEST-FIRST SEARCH - TIC-TAC-TOE

def heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    score = 0

    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        line = [board[a], board[b], board[c]]

        if line.count(player) == 2 and line.count(' ') == 1:
            score += 10

        if line.count(opponent) == 2 and line.count(' ') == 1:
            score -= 10

    return score


def greedy_best_first(board, player):
    best_move = -1
    best_score = -999

    for i in range(9):
        if board[i] == ' ':
            new_board = board[:]
            new_board[i] = player

            score = heuristic(new_board, player)

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


board = [
    'X', 'O', 'X',
    ' ', 'O', ' ',
    ' ', ' ', 'X'
]

move = greedy_best_first(board, 'X')

print("Best move for X is position:", move + 1)

# A* SEARCH - MISSIONARIES AND CANNIBALS

import heapq


def is_valid(state):
    missionaries, cannibals, boat = state

    if missionaries < 0 or missionaries > 3:
        return False

    if cannibals < 0 or cannibals > 3:
        return False

    # Left bank
    if missionaries > 0 and missionaries < cannibals:
        return False

    # Right bank
    right_m = 3 - missionaries
    right_c = 3 - cannibals

    if right_m > 0 and right_m < right_c:
        return False

    return True


def heuristic(state):
    missionaries, cannibals, boat = state
    return missionaries + cannibals


def get_neighbors(state):
    missionaries, cannibals, boat = state

    possible_moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    neighbors = []

    for m, c in possible_moves:

        if boat == 0:
            new_state = (
                missionaries - m,
                cannibals - c,
                1
            )
        else:
            new_state = (
                missionaries + m,
                cannibals + c,
                0
            )

        if is_valid(new_state):
            neighbors.append(new_state)

    return neighbors


def a_star():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (heuristic(start), 0, start, [])
    )

    visited = set()

    while priority_queue:

        f, g, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        new_path = path + [current]

        if current == goal:
            return new_path

        for next_state in get_neighbors(current):

            if next_state not in visited:

                new_g = g + 1
                new_f = new_g + heuristic(next_state)

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, next_state, new_path)
                )

    return None


solution = a_star()

print("Solution:")

for state in solution:
    missionaries, cannibals, boat = state

    print(
        "Missionaries =", missionaries,
        "Cannibals =", cannibals,
        "Boat side =", "Left" if boat == 0 else "Right"
    )



# AO* SEARCH - EIGHT PUZZLE

import heapq


GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_position = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_position] = \
                new_state[new_position], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def ao_star(start):
    priority_queue = []

    heapq.heappush(
        priority_queue,
        (heuristic(start), start)
    )

    parent = {start: None}

    visited = set()

    while priority_queue:

        cost, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == GOAL:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for next_state in get_neighbors(current):

            if next_state not in visited:

                parent[next_state] = current

                heapq.heappush(
                    priority_queue,
                    (heuristic(next_state), next_state)
                )

    return None


start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

solution = ao_star(start)

print("Solution:")

for state in solution:

    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()

# MEMORY-BOUNDED HEURISTIC SEARCH (SMA*) - EIGHT PUZZLE

import heapq


GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1

    return count


def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_position = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_position] = \
                new_state[new_position], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def memory_bounded_search(start, memory_limit=20):

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (heuristic(start), 0, start, [])
    )

    visited = set()

    while priority_queue:

        f, g, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        new_path = path + [current]

        if current == GOAL:
            return new_path

        for next_state in get_neighbors(current):

            if next_state not in visited:

                new_g = g + 1
                new_f = new_g + heuristic(next_state)

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, next_state, new_path)
                )

        # Keep memory within the specified limit
        if len(priority_queue) > memory_limit:

            priority_queue.sort(reverse=True)

            while len(priority_queue) > memory_limit:
                priority_queue.pop()

            heapq.heapify(priority_queue)

    return None


start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

solution = memory_bounded_search(start, 20)

print("Solution:")

for state in solution:

    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()