# Store information about a pizza being ordered.
person = {
    'name': 'tobi',
    'hobbies': ['reading', 'coding', 'designing', 'paring'],
 }

# Greet and start a conversation.
print(f"hello dear {person['name']}, its nice to have you here "
    "\nsuch a nice hobbies you've got:")

for hobby in person['hobbies']:
 print("\t" + hobby)