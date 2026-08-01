# Model-Based Agent: Fully Observable vs Partially Observable

class ModelAgent:
    def __init__(self):
        self.memory = {}

    def act(self, room, status, observable):
        if observable == "Fully":
            self.memory[room] = status
            return "Clean" if status == "Dirty" else "No Action"
        else:
            return "Store previous state and wait"

agent = ModelAgent()

print(agent.act("A", "Dirty", "Fully"))
print(agent.act("B", "Unknown", "Partially"))


# Model-Based Agent: Known vs Unknown

class ModelAgent:
    def act(self, environment):
        if environment == "Known":
            return "Use stored model"
        else:
            return "Learn and update model"

agent = ModelAgent()

print(agent.act("Known"))
print(agent.act("Unknown"))


# Model-Based Agent: Static vs Dynamic

class ModelAgent:
    def act(self, environment):
        if environment == "Static":
            return "Use stored state"
        else:
            return "Update state continuously"

agent = ModelAgent()

print(agent.act("Static"))
print(agent.act("Dynamic"))


# Model-Based Agent: Discrete vs Continuous

class ModelAgent:
    def act(self, environment):
        if environment == "Discrete":
            return "Move to next state"
        else:
            return "Continuously update state"

agent = ModelAgent()

print(agent.act("Discrete"))
print(agent.act("Continuous"))



# Model-Based Agent: Deterministic vs Stochastic

import random

class ModelAgent:
    def act(self, environment):
        if environment == "Deterministic":
            return "Fixed Action"
        else:
            return random.choice(["Action A", "Action B"])

agent = ModelAgent()

print(agent.act("Deterministic"))
print(agent.act("Stochastic"))


# Model-Based Agent: Episodic vs Sequential

class ModelAgent:
    def __init__(self):
        self.history = []

    def act(self, environment, event):
        self.history.append(event)

        if environment == "Episodic":
            return "Solve current episode"
        else:
            return "Use previous history"

agent = ModelAgent()

print(agent.act("Episodic", "Task1"))
print(agent.act("Sequential", "Task2"))