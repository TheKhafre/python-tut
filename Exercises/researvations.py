""" userResponse = int(input('How many people are in your group?: '))

if userResponse > 8:
    print('sorry! there is no available table at the moment; '
          'please wait')
else:
    print('your table is ready') """

toCheck = int(input('enter a number to check: '))

if toCheck % 10 == 0:
    print(f'{toCheck} is a multiple of 10')
else:
    print(f'{toCheck} is not a multiple of 10')