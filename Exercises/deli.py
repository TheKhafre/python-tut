sandwich_order = ['tuna', 'chicken', 'brown', 'crispy']
finished_sandwich = []

while sandwich_order:
    making = sandwich_order.pop()
    print(f'currently making {making} sandwich')

    finished_sandwich.append(making)

print('\nthe finished sandwiches are: ')
for sandwich in finished_sandwich:
    print(f'{sandwich} sandwich')