pizza = {
    'crust' : 'thick',
    'toppings' : ['mushroom', 'extra cheese']
}

print(f'you ordered a {pizza['crust']}-crust pizza '
      'with the following toppings:')

for topping in pizza['toppings']:
    print(f'\t - {topping}')

print('\n')