

# 1. Fully Observable Environment


### Example: Robot choosing the best route


class FullyObservableUtilityAgent:
    def __init__(self, goal):
        self.goal = goal

    def calculate_utility(self, action):
        utilities = {
            "Fast Route": 70,
            "Safe Route": 90,
            "Short Route": 80
        }

        return utilities[action]

    def choose_action(self, actions):
        best_action = max(
            actions,
            key=self.calculate_utility
        )

        return best_action


# Agent
agent = FullyObservableUtilityAgent(goal="Destination")

actions = [
    "Fast Route",
    "Safe Route",
    "Short Route"
]

best_action = agent.choose_action(actions)

print("Available Actions:", actions)
print("Selected Action:", best_action)
print("Utility:", agent.calculate_utility(best_action))


# 2. Partially Observable Environment


### Example: Robot deciding whether to move


class PartiallyObservableUtilityAgent:
    def __init__(self):
        self.belief_state = {}

    def update_belief(self, observation):
        self.belief_state = observation

    def calculate_utility(self, action):
        if self.belief_state["obstacle"]:

            utilities = {
                "Move Forward": 20,
                "Turn Left": 80,
                "Turn Right": 70
            }

        else:

            utilities = {
                "Move Forward": 90,
                "Turn Left": 60,
                "Turn Right": 50
            }

        return utilities[action]

    def choose_action(self, actions):
        return max(
            actions,
            key=self.calculate_utility
        )


agent = PartiallyObservableUtilityAgent()

# Agent receives observation
observation = {
    "obstacle": True
}

agent.update_belief(observation)

actions = [
    "Move Forward",
    "Turn Left",
    "Turn Right"
]

best_action = agent.choose_action(actions)

print("Observation:", observation)
print("Selected Action:", best_action)
print("Utility:", agent.calculate_utility(best_action))


# 3. Known Environment


class KnownUtilityAgent:
    def __init__(self):
        self.environment = {
            "A": {
                "Go to B": 60,
                "Go to C": 80,
                "Go to D": 50
            }
        }

    def choose_action(self, current_state):
        actions = self.environment[current_state]

        best_action = max(
            actions,
            key=actions.get
        )

        return best_action, actions[best_action]


agent = KnownUtilityAgent()

action, utility = agent.choose_action("A")

print("Current State: A")
print("Selected Action:", action)
print("Utility:", utility)


# 4. Unknown Environment


class UnknownUtilityAgent:
    def __init__(self):
        self.utility_estimates = {}

    def choose_action(self, actions):
        # Explore unknown actions
        for action in actions:
            if action not in self.utility_estimates:
                return action

        # Choose action with highest learned utility
        return max(
            actions,
            key=lambda x: self.utility_estimates[x]
        )

    def learn(self, action, received_utility):
        self.utility_estimates[action] = received_utility


agent = UnknownUtilityAgent()

actions = [
    "Action A",
    "Action B",
    "Action C"
]

# Agent explores
for i in range(3):

    action = agent.choose_action(actions)

    print("Chosen Action:", action)

    # Environment returns utility
    utility = {
        "Action A": 50,
        "Action B": 90,
        "Action C": 70
    }[action]

    print("Received Utility:", utility)

    agent.learn(action, utility)


print("\nLearned Utilities:")
print(agent.utility_estimates)

best_action = agent.choose_action(actions)

print("Best Action:", best_action)





# 5. Static Environment


### Example: Choosing a house


class StaticUtilityAgent:
    def __init__(self):
        self.houses = {
            "House A": 70,
            "House B": 90,
            "House C": 80
        }

    def choose_house(self):
        best_house = max(
            self.houses,
            key=self.houses.get
        )

        return best_house


agent = StaticUtilityAgent()

best_house = agent.choose_house()

print("Available Houses:")
print(agent.houses)

print("Best Choice:", best_house)
print("Utility:", agent.houses[best_house])


# 6. Dynamic Environment
### Example: Self-driving car


class DynamicUtilityAgent:
    def calculate_utility(self, traffic, weather):

        if traffic == "Low" and weather == "Clear":
            return {
                "Fast Route": 90,
                "Safe Route": 80
            }

        elif traffic == "High":
            return {
                "Fast Route": 40,
                "Safe Route": 90
            }

        elif weather == "Rain":
            return {
                "Fast Route": 50,
                "Safe Route": 95
            }

    def choose_action(self, traffic, weather):

        utilities = self.calculate_utility(
            traffic,
            weather
        )

        return max(
            utilities,
            key=utilities.get
        )


agent = DynamicUtilityAgent()

environment_conditions = [
    ("Low", "Clear"),
    ("High", "Clear"),
    ("Low", "Rain")
]

for traffic, weather in environment_conditions:

    action = agent.choose_action(
        traffic,
        weather
    )

    print(
        "Traffic:", traffic,
        "| Weather:", weather,
        "| Selected:", action
    )



# 7. Discrete Environment

### Example: Game agent


class DiscreteUtilityAgent:
    def __init__(self):
        self.utilities = {
            "Move Left": 50,
            "Move Right": 80,
            "Attack": 90,
            "Defend": 70
        }

    def choose_action(self):
        return max(
            self.utilities,
            key=self.utilities.get
        )


agent = DiscreteUtilityAgent()

action = agent.choose_action()

print("Available Actions:")
print(agent.utilities)

print("Best Action:", action)
print("Utility:", agent.utilities[action])


# 8. Continuous Environment


### Example: Robot choosing movement speed

class ContinuousUtilityAgent:

    def calculate_utility(self, speed):

        # Higher speed gives more reward
        speed_reward = speed * 10

        # High speed reduces safety
        safety_penalty = speed ** 2

        utility = speed_reward - safety_penalty

        return utility

    def choose_speed(self):

        best_speed = 0
        best_utility = float("-inf")

        # Test continuous range
        speed = 0

        while speed <= 10:

            utility = self.calculate_utility(speed)

            if utility > best_utility:
                best_utility = utility
                best_speed = speed

            speed += 0.1

        return best_speed, best_utility


agent = ContinuousUtilityAgent()

speed, utility = agent.choose_speed()

print("Best Speed:", round(speed, 1))
print("Maximum Utility:", round(utility, 2))


# 9. Deterministic Environment

### Example

class DeterministicUtilityAgent:

    def __init__(self):

        self.actions = {
            "Move A": {
                "utility": 50,
                "result": "State A"
            },

            "Move B": {
                "utility": 90,
                "result": "Goal"
            },

            "Move C": {
                "utility": 70,
                "result": "State C"
            }
        }

    def choose_action(self):

        best_action = max(
            self.actions,
            key=lambda x: self.actions[x]["utility"]
        )

        return best_action


agent = DeterministicUtilityAgent()

action = agent.choose_action()

print("Selected Action:", action)
print("Expected Result:", agent.actions[action]["result"])
print("Utility:", agent.actions[action]["utility"])


# 10. Stochastic Environment



### Python implementation

class StochasticUtilityAgent:

    def calculate_expected_utility(self, outcomes):

        expected_utility = 0

        for probability, utility in outcomes:
            expected_utility += probability * utility

        return expected_utility

    def choose_action(self, actions):

        expected_utilities = {}

        for action, outcomes in actions.items():

            expected_utilities[action] = \
                self.calculate_expected_utility(outcomes)

        best_action = max(
            expected_utilities,
            key=expected_utilities.get
        )

        return best_action, expected_utilities


agent = StochasticUtilityAgent()

actions = {

    "Action A": [
        (0.8, 100),
        (0.2, 20)
    ],

    "Action B": [
        (0.5, 150),
        (0.5, 40)
    ],

    "Action C": [
        (1.0, 70)
    ]
}

best_action, expected_utilities = \
    agent.choose_action(actions)

print("Expected Utilities:")

for action, utility in expected_utilities.items():
    print(action, ":", utility)

print("\nBest Action:", best_action)


# 11. Episodic Environment


### Example: Medical diagnosis or image classification


class EpisodicUtilityAgent:

    def choose_action(self, image):

        utilities = {
            "Cat": 0,
            "Dog": 0,
            "Unknown": 0
        }

        if image == "Cat":
            utilities["Cat"] = 100
            utilities["Dog"] = 20

        elif image == "Dog":
            utilities["Dog"] = 100
            utilities["Cat"] = 20

        else:
            utilities["Unknown"] = 80

        return max(
            utilities,
            key=utilities.get
        )


agent = EpisodicUtilityAgent()

episodes = [
    "Cat",
    "Dog",
    "Unknown"
]

for episode in episodes:

    action = agent.choose_action(episode)

    print(
        "Episode Input:",
        episode,
        "| Decision:",
        action
    )


# 12. Sequential Environment


### Example: Route planning

class SequentialUtilityAgent:

    def __init__(self):

        self.routes = {

            "A": {
                "Go to B": 50,
                "Go to C": 80
            },

            "B": {
                "Go to D": 60
            },

            "C": {
                "Go to D": 90
            }
        }

    def choose_action(self, current_state):

        actions = self.routes[current_state]

        best_action = max(
            actions,
            key=actions.get
        )

        return best_action, actions[best_action]


agent = SequentialUtilityAgent()

current_state = "A"

while current_state != "D":

    action, utility = \
        agent.choose_action(current_state)

    print(
        "State:", current_state,
        "| Action:", action,
        "| Utility:", utility
    )

    # Move to next state
    if action == "Go to B":
        current_state = "B"

    elif action == "Go to C":
        current_state = "C"

    elif action == "Go to D":
        current_state = "D"

print("Final State:", current_state)

