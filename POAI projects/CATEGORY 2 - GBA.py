

## 1. Fully Observable Environment

#**Example:** A robot moving on a grid where it can see the complete environment.

class FullyObservableAgent:
    def __init__(self, goal):
        self.goal = goal

    def choose_action(self, current_position):
        x, y = current_position
        gx, gy = self.goal

        if current_position == self.goal:
            return "Goal Reached"

        if x < gx:
            return "Move Right"
        elif x > gx:
            return "Move Left"
        elif y < gy:
            return "Move Down"
        elif y > gy:
            return "Move Up"


# Environment
agent = FullyObservableAgent(goal=(3, 3))

current_position = (0, 0)

while current_position != agent.goal:
    action = agent.choose_action(current_position)
    print("Position:", current_position, "Action:", action)

    x, y = current_position

    if action == "Move Right":
        x += 1
    elif action == "Move Left":
        x -= 1
    elif action == "Move Down":
        y += 1
    elif action == "Move Up":
        y -= 1

    current_position = (x, y)

print("Goal Reached!")


# 2. Partially Observable Environment

#**Example:** A robot cannot see its exact position. It only receives observations.


class PartiallyObservableAgent:
    def __init__(self, goal):
        self.goal = goal
        self.belief_state = 0

    def observe(self, observation):
        # Agent updates its belief using the observation
        if observation == "Near Goal":
            self.belief_state = 1
        else:
            self.belief_state = 0

    def choose_action(self):
        if self.belief_state == 1:
            return "Move Forward"
        else:
            return "Search for Goal"


# Environment
agent = PartiallyObservableAgent(goal="Target")

observations = [
    "Unknown",
    "Unknown",
    "Near Goal"
]

for observation in observations:
    agent.observe(observation)
    action = agent.choose_action()

    print("Observation:", observation)
    print("Action:", action)


# 3. Known Environment

#**Example:** The agent knows all possible states and actions.

class KnownEnvironmentAgent:
    def __init__(self, goal):
        self.goal = goal

    def choose_action(self, current_state, environment):
        if current_state == self.goal:
            return "Goal Reached"

        for action, next_state in environment[current_state]:
            if next_state == self.goal:
                return action

        # Choose the first available action
        return environment[current_state][0][0]


# Known environment
environment = {
    "A": [
        ("Go to B", "B"),
        ("Go to C", "C")
    ],
    "B": [
        ("Go to D", "D")
    ],
    "C": [
        ("Go to D", "D")
    ],
    "D": []
}

agent = KnownEnvironmentAgent("D")

current_state = "A"

while current_state != agent.goal:
    action = agent.choose_action(current_state, environment)

    print("Current State:", current_state)
    print("Action:", action)

    # Find next state
    for a, next_state in environment[current_state]:
        if a == action:
            current_state = next_state
            break

print("Goal Reached!")

# 4. Unknown Environment

#**Example:** The agent does not know where actions will take it. It learns while exploring.
class UnknownEnvironmentAgent:
    def __init__(self, goal):
        self.goal = goal
        self.known_environment = {}

    def learn(self, current_state, action, next_state):
        if current_state not in self.known_environment:
            self.known_environment[current_state] = {}

        self.known_environment[current_state][action] = next_state

    def choose_action(self, current_state):
        # Explore if state is unknown
        if current_state not in self.known_environment:
            return "Explore"

        # Use known actions
        for action, next_state in self.known_environment[current_state].items():
            if next_state == self.goal:
                return action

        return "Explore"


agent = UnknownEnvironmentAgent("D")

# Agent explores the environment
experiences = [
    ("A", "Move Right", "B"),
    ("B", "Move Right", "C"),
    ("C", "Move Right", "D")
]

for current_state, action, next_state in experiences:
    print("Agent at:", current_state)
    print("Agent learns:", action, "leads to", next_state)

    agent.learn(current_state, action, next_state)

print("\nKnown Environment:")
print(agent.known_environment)


# 5. Static Environment

#**Example:** A crossword puzzle.


class StaticGoalAgent:
    def __init__(self, goal):
        self.goal = goal

    def solve(self, current_state):
        print("Current State:", current_state)

        if current_state == self.goal:
            return "Goal Already Achieved"

        return "Solve the Puzzle"


agent = StaticGoalAgent("Completed")

current_state = "Incomplete"

print(agent.solve(current_state))

# Agent solves the puzzle
current_state = "Completed"

print(agent.solve(current_state))


# 6. Dynamic Environment

#**Example:** A self-driving car where other vehicles can move.

class DynamicGoalAgent:
    def __init__(self, goal):
        self.goal = goal

    def choose_action(self, current_position, traffic):
        if current_position == self.goal:
            return "Goal Reached"

        if traffic == "Heavy":
            return "Wait"

        if traffic == "Clear":
            return "Move Forward"

        return "Recalculate Route"


agent = DynamicGoalAgent(goal=10)

current_position = 0

traffic_conditions = [
    "Clear",
    "Heavy",
    "Clear",
    "Clear"
]

for traffic in traffic_conditions:

    action = agent.choose_action(
        current_position,
        traffic
    )

    print(
        "Position:", current_position,
        "| Traffic:", traffic,
        "| Action:", action
    )

    if action == "Move Forward":
        current_position += 1

    if current_position == agent.goal:
        print("Goal Reached!")
        break




# 7. Discrete Environment

#**Example:** A chess-like board where positions are discrete cells.

class DiscreteGoalAgent:
    def __init__(self, goal):
        self.goal = goal

    def choose_action(self, current_position):
        if current_position == self.goal:
            return "Goal Reached"

        return "Move to Next Cell"


agent = DiscreteGoalAgent(goal=5)

current_position = 0

while current_position < agent.goal:
    action = agent.choose_action(current_position)

    print(
        "Position:", current_position,
        "Action:", action
    )

    current_position += 1

print("Goal Reached!")


# 8. Continuous Environment

#**Example:** A robot moving continuously toward a target.

class ContinuousGoalAgent:
    def __init__(self, goal, step=0.5):
        self.goal = goal
        self.step = step

    def choose_action(self, position):
        if abs(position - self.goal) < 0.01:
            return "Stop"

        if position < self.goal:
            return "Move Right"

        return "Move Left"


agent = ContinuousGoalAgent(goal=5.0)

position = 0.0

while abs(position - agent.goal) > 0.01:

    action = agent.choose_action(position)

    print(
        "Position:", round(position, 2),
        "Action:", action
    )

    if action == "Move Right":
        position += agent.step

    elif action == "Move Left":
        position -= agent.step

print("Goal Reached at:", position)


# 9. Deterministic Environment

#**Example:** 8-puzzle where every action has a predictable result.

class DeterministicAgent:
    def __init__(self, goal):
        self.goal = goal

    def choose_action(self, current_state):
        if current_state == self.goal:
            return "Goal Reached"

        return "Move to Goal"


agent = DeterministicAgent(goal="B")

current_state = "A"

while current_state != agent.goal:

    action = agent.choose_action(current_state)

    print(
        "State:", current_state,
        "Action:", action
    )

    # Action always produces the same result
    if action == "Move to Goal":
        current_state = "B"

print("Goal Reached!")

# 10. Stochastic Environment

#**Example:** A robot tries to move forward, but there is a probability that it slips.

import random


class StochasticGoalAgent:
    def __init__(self, goal):
        self.goal = goal

    def choose_action(self, position):
        if position == self.goal:
            return "Stop"

        return "Move Forward"


agent = StochasticGoalAgent(goal=5)

position = 0

while position < agent.goal:

    action = agent.choose_action(position)

    print("Position:", position)
    print("Action:", action)

    # Random outcome
    success = random.choice([True, False])

    if success:
        position += 1
        print("Result: Successful movement")
    else:
        print("Result: Movement failed")

print("Goal Reached!")

# 11. Episodic Environment

#**Example:** An image classification agent. Each image is an independent episode.
class EpisodicGoalAgent:
    def __init__(self):
        self.goal = "Correct Classification"

    def classify(self, image):
        # Simple example
        if image == "Cat":
            return "Cat"
        elif image == "Dog":
            return "Dog"

        return "Unknown"

    def check_goal(self, image, prediction):
        return image == prediction


agent = EpisodicGoalAgent()

images = ["Cat", "Dog", "Cat"]

for image in images:

    prediction = agent.classify(image)

    if agent.check_goal(image, prediction):
        print(
            "Image:", image,
            "| Prediction:", prediction,
            "| Goal Achieved"
        )
    else:
        print(
            "Image:", image,
            "| Prediction:", prediction,
            "| Goal Failed"
        )


# 12. Sequential Environment

#Example:** A route-finding agent. Every action affects the next state.

class SequentialGoalAgent:
    def __init__(self, goal):
        self.goal = goal

    def choose_action(self, current_state):
        route = {
            "A": ("Go to B", "B"),
            "B": ("Go to C", "C"),
            "C": ("Go to D", "D")
        }

        if current_state == self.goal:
            return "Goal Reached", current_state

        return route[current_state]


agent = SequentialGoalAgent(goal="D")

current_state = "A"

while current_state != agent.goal:

    action, next_state = agent.choose_action(current_state)

    print(
        "Current State:", current_state,
        "| Action:", action,
        "| Next State:", next_state
    )

    current_state = next_state

print("Final Goal Reached!")
