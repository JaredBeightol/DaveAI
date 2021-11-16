# DAVE AI
# This is a project and an attempt for me to create an AI
# There isn't really an end goal, this is more an experiment
# Started on 11/16/2021

# DECLARE VARIABLES HERE
userInputs = []  # List to hold user inputs
AIObservations = []  # List to hold all of DaveAI's knowledge

# Prompts user
print("Hello! Welcome to DaveAI. This AI is attempting to learn by observation, so go ahead! Feel free to interact.")

# Interaction and processing loop
while True:
    userInput = input()  # Gets user input
    userInputs.append(userInput)  # Adds user input to list of user inputs
    AIObservations.append(userInput)  # AI Observes recent user input

    # Just testing boiler plate code
    print(len(userInputs))
    print(userInputs.pop())
    print(len(userInputs))
