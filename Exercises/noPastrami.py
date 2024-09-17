sandwich_order = ['tuna', 'pastrami', 'chicken', 'pastrami', 'pastrami', 'brown', 'crispy']
finished_sandwich = []

print('\nSorry! we have run out of pastrami sandwich\n')
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    making = sandwich_order.pop()
    print(f'currently making {making} sandwich')

    finished_sandwich.append(making)

print('\nthe finished sandwiches are: ')
for sandwich in finished_sandwich:
    print(f'{sandwich} sandwich')