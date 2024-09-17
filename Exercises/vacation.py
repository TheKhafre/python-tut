vacay_spot = {}

while True:
    name = input('\ntell us your name: ')
    spot = input('what vacation spot do you have in mind: ')

    vacay_spot[name] = spot

    retry = input('want to enter another entry?(yes/no) ')
    if retry.lower() == 'no':
        break

print('\n')
for name, spot in vacay_spot.items():
    print(f'{name.title()} wants to visit {spot.title()}')