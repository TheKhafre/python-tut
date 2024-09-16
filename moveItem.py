unconfirmed_users = ['femi', 'daniel', 'feyi', 'tobi']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'verifying user: {current_user.title()}')
    
    if current_user == 'daniel':
        continue
    else:
        confirmed_users.append(current_user)

print('\nthe confirmed users are: ')
for users in confirmed_users:
    print(f'\t - {users.title()}')