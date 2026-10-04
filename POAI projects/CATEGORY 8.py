# Medical Diagnosis using Knowledge Base
# Facts, Rules, Forward Chaining and Backward Chaining


# -----------------------------
# KNOWLEDGE BASE
# -----------------------------

facts = {
    "fever",
    "cough",
    "body_pain"
}

rules = [
    ({"fever", "cough", "body_pain"}, "flu"),
    ({"fever", "rash"}, "measles"),
    ({"cough", "breathing_difficulty"}, "respiratory_infection"),
    ({"fever", "headache"}, "viral_fever")
]


# -----------------------------
# FORWARD CHAINING
# -----------------------------

def forward_chaining(facts, rules):

    inferred = set(facts)

    changed = True

    while changed:
        changed = False

        for conditions, conclusion in rules:

            if conditions.issubset(inferred):
                if conclusion not in inferred:

                    inferred.add(conclusion)

                    print(
                        "Rule fired:",
                        conditions,
                        "->",
                        conclusion
                    )

                    changed = True

    return inferred


# -----------------------------
# BACKWARD CHAINING
# -----------------------------

def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    # Goal is already a fact
    if goal in facts:
        return True

    # Avoid infinite loops
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules that can produce the goal
    for conditions, conclusion in rules:

        if conclusion == goal:

            # Check whether all conditions can be proved
            if all(
                backward_chaining(
                    condition,
                    facts,
                    rules,
                    visited
                )
                for condition in conditions
            ):
                return True

    return False


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("Initial Facts:")
print(facts)

print("\n--- FORWARD CHAINING ---")

inferred_facts = forward_chaining(facts, rules)

print("\nAll Inferred Facts:")
print(inferred_facts)


print("\n--- BACKWARD CHAINING ---")

goal = "flu"

if backward_chaining(goal, facts, rules):
    print("Goal", goal, "can be proved.")
else:
    print("Goal", goal, "cannot be proved.")

# Autonomous Vehicle using Knowledge Base
# Facts, Rules, Forward Chaining and Backward Chaining


# -----------------------------
# KNOWLEDGE BASE
# -----------------------------

facts = {
    "high_speed",
    "obstacle_detected",
    "traffic_light_red"
}


rules = [
    ({"obstacle_detected"}, "brake"),
    ({"traffic_light_red"}, "stop"),
    ({"high_speed", "obstacle_detected"}, "emergency_brake"),
    ({"traffic_light_green", "no_obstacle"}, "move"),
    ({"obstacle_detected"}, "slow_down")
]


# -----------------------------
# FORWARD CHAINING
# -----------------------------

def forward_chaining(facts, rules):

    inferred = set(facts)

    changed = True

    while changed:

        changed = False

        for conditions, conclusion in rules:

            if conditions.issubset(inferred):

                if conclusion not in inferred:

                    inferred.add(conclusion)

                    print(
                        "Rule fired:",
                        conditions,
                        "->",
                        conclusion
                    )

                    changed = True

    return inferred


# -----------------------------
# BACKWARD CHAINING
# -----------------------------

def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    # Goal already known
    if goal in facts:
        return True

    if goal in visited:
        return False

    visited.add(goal)

    for conditions, conclusion in rules:

        if conclusion == goal:

            if all(
                backward_chaining(
                    condition,
                    facts,
                    rules,
                    visited
                )
                for condition in conditions
            ):
                return True

    return False


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("Initial Vehicle Facts:")
print(facts)

print("\n--- FORWARD CHAINING ---")

inferred = forward_chaining(facts, rules)

print("\nInferred Actions:")
print(inferred)


print("\n--- BACKWARD CHAINING ---")

goal = "emergency_brake"

if backward_chaining(goal, facts, rules):

    print(
        "Goal",
        goal,
        "can be achieved."
    )

else:

    print(
        "Goal",
        goal,
        "cannot be achieved."
    )

# Industrial Manufacturing using Knowledge Base
# Facts, Rules, Forward Chaining and Backward Chaining


# -----------------------------
# KNOWLEDGE BASE
# -----------------------------

facts = {
    "machine_running",
    "high_temperature",
    "low_pressure"
}


rules = [
    ({"high_temperature"}, "overheating"),
    ({"low_pressure"}, "pressure_warning"),
    ({"overheating", "low_pressure"}, "machine_fault"),
    ({"machine_fault"}, "maintenance_required"),
    ({"machine_fault"}, "stop_machine")
]


# -----------------------------
# FORWARD CHAINING
# -----------------------------

def forward_chaining(facts, rules):

    inferred = set(facts)

    changed = True

    while changed:

        changed = False

        for conditions, conclusion in rules:

            if conditions.issubset(inferred):

                if conclusion not in inferred:

                    inferred.add(conclusion)

                    print(
                        "Rule fired:",
                        conditions,
                        "->",
                        conclusion
                    )

                    changed = True

    return inferred


# -----------------------------
# BACKWARD CHAINING
# -----------------------------

def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    # Goal is already a fact
    if goal in facts:
        return True

    # Prevent loops
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules that produce the goal
    for conditions, conclusion in rules:

        if conclusion == goal:

            if all(
                backward_chaining(
                    condition,
                    facts,
                    rules,
                    visited
                )
                for condition in conditions
            ):
                return True

    return False


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("Initial Machine Facts:")
print(facts)

print("\n--- FORWARD CHAINING ---")

inferred = forward_chaining(facts, rules)

print("\nAll Inferred Facts:")
print(inferred)


print("\n--- BACKWARD CHAINING ---")

goal = "maintenance_required"

if backward_chaining(goal, facts, rules):

    print(
        "Goal",
        goal,
        "can be proved."
    )

else:

    print(
        "Goal",
        goal,
        "cannot be proved."
    )