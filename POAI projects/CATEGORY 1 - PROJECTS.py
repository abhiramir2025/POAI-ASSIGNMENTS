'''CATEGORY 1 - PROJECTS'''
#SRA & MBA - Automatic Vacuum Cleaner
def simple_reflex_agent(percept):
    if percept == "Dirty":
        return "Suck"
    else:
        return "No Action"

# Test
print(simple_reflex_agent("Dirty"))
print(simple_reflex_agent("Clean"))


class ModelBasedAgent:
    def __init__(self):
        self.state = {}

    def act(self, location, status):
        self.state[location] = status

        if status == "Dirty":
            return "Suck"
        else:
            return "Move"

agent = ModelBasedAgent()

print(agent.act("A", "Dirty"))
print(agent.act("B", "Clean"))



# Goal-Based Agent - Robot reaching a goal

goal = 10

class GoalBasedAgent:

    def __init__(self):
        self.position = 0

    def move(self):
        if self.position < goal:
            self.position += 1
            print("Moving Forward...")
        else:
            print("Goal Reached!")

# Main Program
agent = GoalBasedAgent()

while agent.position < goal:
    print("Current Position:", agent.position)
    agent.move()

print("Final Position:", agent.position)
print("Goal Achieved!")


# Utility-Based Agent - Simple Route selection

routes = {
    "Route A": 60,
    "Route B": 90,
    "Route C": 75
}

class UtilityBasedAgent:

    def choose_best_route(self):
        best_route = max(routes, key=routes.get)
        return best_route

# Main Program
agent = UtilityBasedAgent()

route = agent.choose_best_route()

print("Available Routes:")
print(routes)

print("\nBest Route:", route)
print("Utility:", routes[route])