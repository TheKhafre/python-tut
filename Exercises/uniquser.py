current_users = ['femi', 'daniel', 'segun', 'idris']
new_users = ['gloria', 'daniel', 'segun', 'james']

for users in new_users:
    if users.lower() in current_users:
        print(f"Sorry {users}, that name is taken.")
    else:
        print(f"Great, {users} is still available.")