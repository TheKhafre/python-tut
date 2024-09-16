# The program checks new user for user that already exists in the database

current_users = [
    "samuel",
    "john",
    "alex",
    "ora",
    "Dolapo"
]

new_users = [
    "Ayoka",
    "Adunni",
    "alex",
    "ORA",
    "James"
]

for user in new_users:
     # converts new entry to lower case
     # assuming current is already in lowercase
     # else, we can also add .lower to current_users
    if user.lower() in current_users:
        print(f"{user} already exist")
    else:
        print(f"{user} account created successfully")