# Bayesian Reasoning for Medical Diagnosis

prior_disease = 0.01
prior_no_disease = 0.99

sensitivity = 0.90
false_positive = 0.05

positive_test = (
    sensitivity * prior_disease
    + false_positive * prior_no_disease
)

posterior = (
    sensitivity * prior_disease
    / positive_test
)

print("Probability of disease:",
      round(posterior * 100, 2), "%")

if posterior > 0.5:
    print("Diagnosis: Disease likely")
else:
    print("Diagnosis: Disease unlikely")


# Fuzzy Inferencing for Smart Manufacturing

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
temperature = ctrl.Antecedent(
    np.arange(0, 101, 1), 'temperature'
)

vibration = ctrl.Antecedent(
    np.arange(0, 101, 1), 'vibration'
)

# Output variable
risk = ctrl.Consequent(
    np.arange(0, 101, 1), 'risk'
)

# Membership functions
temperature['low'] = fuzz.trimf(
    temperature.universe, [0, 0, 50]
)

temperature['high'] = fuzz.trimf(
    temperature.universe, [30, 100, 100]
)

vibration['low'] = fuzz.trimf(
    vibration.universe, [0, 0, 50]
)

vibration['high'] = fuzz.trimf(
    vibration.universe, [30, 100, 100]
)

risk['low'] = fuzz.trimf(
    risk.universe, [0, 0, 50]
)

risk['high'] = fuzz.trimf(
    risk.universe, [50, 100, 100]
)

# Fuzzy rules
rule1 = ctrl.Rule(
    temperature['low'] & vibration['low'],
    risk['low']
)

rule2 = ctrl.Rule(
    temperature['high'] | vibration['high'],
    risk['high']
)

# Create control system
system = ctrl.ControlSystem([rule1, rule2])

simulation = ctrl.ControlSystemSimulation(system)

# Input values
simulation.input['temperature'] = 80
simulation.input['vibration'] = 70

# Compute output
simulation.compute()

print("Machine Risk:",
      round(simulation.output['risk'], 2))

if simulation.output['risk'] > 50:
    print("Decision: Maintenance Required")
else:
    print("Decision: Machine Normal")