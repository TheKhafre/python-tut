""" pizza = {
    'crust' : 'thick',
    'toppings' : ['mushroom', 'extra cheese']
}

print(f'you ordered a {pizza['crust']}-crust pizza '
      'with the following toppings:')

for topping in pizza['toppings']:
    print(f'\t - {topping}')

print('\n') """

""" favorite_languages = {
    'tobi': ['c', 'python', 'javascript'],
    'femi': ['python', 'go'],
    'feyi': ['c', 'javascript'],
    'bose': ['javascript']
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")

    else:
        print(f"\n{name.title()}'s favorite languages are:")
    
    for language in languages:
        print(f'\t{language.title()}') """

# Nesting a dictionary inside a dictionary
users = {
    'fabulous' : {
        'first' : 'femi',
        'last' : 'adebayo',
        'location' : 'ondo'
    },

    'Khafre' : {
        'first' : 'tobi',
        'last' : 'olajide',
        'location' : 'lagos'
    },

    'Danno' : {
        'first' : 'Olusegun',
        'last' : 'Ayodeji',
        'location' : 'Otan'
    },
}

for name, user_info in users.items():
    print(f'\n Username: {name.title()}')
    for value in user_info.values():
        print(f'\t{value.title()}')
    """ print(f'\t fullname: {user_info['first'].title()} {user_info['last'].title()} ')
    print(f'\t location: {user_info['location'].title()}') """