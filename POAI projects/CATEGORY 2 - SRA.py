# Fully Observable vs Partially Observable

def reflex_agent(observation, fully_observable):
    if fully_observable:
        if observation == "Dirty":
            return "Clean"
        else:
            return "No Action"
    else:
        return "Cannot decide - Need more information"

print("Fully Observable:", reflex_agent("Dirty", True))
print("Partially Observable:", reflex_agent("Unknown", False))


# Known vs Unknown Environment

def reflex_agent(environment):
    if environment == "Known":
        return "Perform predefined action"
    else:
        return "Explore the environment"

print(reflex_agent("Known"))
print(reflex_agent("Unknown"))


# Static vs Dynamic Environment

def reflex_agent(environment):
    if environment == "Static":
        return "Take action"
    else:
        return "Observe and update action"

print(reflex_agent("Static"))
print(reflex_agent("Dynamic"))

# Discrete vs Continuous Environment

def reflex_agent(environment):
    if environment == "Discrete":
        return "Move to next state"
    else:
        return "Continuously monitor"

print(reflex_agent("Discrete"))
print(reflex_agent("Continuous"))


import random

def reflex_agent(environment):
    if environment == "Deterministic":
        return "Same action every time"
    else:
        return random.choice(["Action A", "Action B"])

print(reflex_agent("Deterministic"))
print(reflex_agent("Stochastic"))


# Episodic vs Sequential Environment

def reflex_agent(environment):
    if environment == "Episodic":
        return "Handle current task only"
    else:
        return "Consider previous actions"

print(reflex_agent("Episodic"))
print(reflex_agent("Sequential"))