# Map Coloring using CSP and Backtracking

regions = ['A', 'B', 'C', 'D', 'E']

colors = ['Red', 'Green', 'Blue']

# Adjacent regions
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

assignment = {}


def is_safe(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve():
    # All regions are colored
    if len(assignment) == len(regions):
        return True

    # Select an unassigned region
    for region in regions:
        if region not in assignment:
            break

    # Try every color
    for color in colors:
        if is_safe(region, color):
            assignment[region] = color

            if solve():
                return True

            # Backtrack
            del assignment[region]

    return False


if solve():
    print("Map Coloring Solution:")
    for region in regions:
        print(region, "->", assignment[region])
else:
    print("No solution exists.")


# Crypt-Arithmetic Puzzle
# SEND + MORE = MONEY

from itertools import permutations

letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

digits = range(10)

solution = None

for values in permutations(digits, len(letters)):

    assignment = dict(zip(letters, values))

    # S and M cannot be zero
    if assignment['S'] == 0 or assignment['M'] == 0:
        continue

    SEND = (
        assignment['S'] * 1000 +
        assignment['E'] * 100 +
        assignment['N'] * 10 +
        assignment['D']
    )

    MORE = (
        assignment['M'] * 1000 +
        assignment['O'] * 100 +
        assignment['R'] * 10 +
        assignment['E']
    )

    MONEY = (
        assignment['M'] * 10000 +
        assignment['O'] * 1000 +
        assignment['N'] * 100 +
        assignment['E'] * 10 +
        assignment['Y']
    )

    if SEND + MORE == MONEY:
        solution = assignment
        break


if solution:
    print("Solution Found:")
    
    for letter in letters:
        print(letter, "=", solution[letter])

    print("\nVerification:")
    print("SEND =", SEND)
    print("MORE =", MORE)
    print("MONEY =", MONEY)
    print(SEND, "+", MORE, "=", MONEY)

else:
    print("No solution exists.")


# Local Search for CSP using Min-Conflicts

import random

regions = ['A', 'B', 'C', 'D', 'E']

colors = ['Red', 'Green', 'Blue']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}


# Generate a random assignment
assignment = {
    region: random.choice(colors)
    for region in regions
}


def conflicts(region, color):
    count = 0

    for neighbor in neighbors[region]:
        if assignment[neighbor] == color:
            count += 1

    return count


def total_conflicts():
    count = 0

    for region in regions:
        count += conflicts(region, assignment[region])

    # Each conflict is counted twice
    return count // 2


def min_conflicts(max_steps=100):

    for step in range(max_steps):

        # Check if solution is found
        if total_conflicts() == 0:
            return True, step

        # Select a conflicted variable
        conflicted = [
            region for region in regions
            if conflicts(region, assignment[region]) > 0
        ]

        if not conflicted:
            return True, step

        region = random.choice(conflicted)

        # Find colors producing minimum conflicts
        conflict_values = {}

        for color in colors:
            conflict_values[color] = conflicts(region, color)

        minimum = min(conflict_values.values())

        best_colors = [
            color for color in colors
            if conflict_values[color] == minimum
        ]

        # Assign one of the best colors
        assignment[region] = random.choice(best_colors)

    return False, max_steps


print("Initial Assignment:")
print(assignment)

print("\nInitial Conflicts:", total_conflicts())

success, steps = min_conflicts()

print("\nFinal Assignment:")
for region in regions:
    print(region, "->", assignment[region])

print("\nFinal Conflicts:", total_conflicts())
print("Steps:", steps)

if success:
    print("\nSolution Found!")
else:
    print("\nSolution not found within step limit.")