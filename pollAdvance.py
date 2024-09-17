responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Mountain you would like to climb someday? ")

    # store the responses in the dictionary.
    responses[name] = response

    repeat = input("Have another response? (yes/ no): ")
    if repeat.lower() == 'no':
        break

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")