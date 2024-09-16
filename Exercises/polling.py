aliens = []

for alien_num in range(8):
    slow_alien = {'color' : 'green', 'point' : 5, 'speed' : 'slow'}
    fast_alien = {'color' : 'blue', 'point' : 10, 'speed' : 'fast'}

    if alien_num % 2 == 0:
        aliens.append(slow_alien)
    elif alien_num % 2 == 1:
        aliens.append(fast_alien)

for alien in aliens[3:7]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 8
        alien['speed'] = 'medium'

for alien in aliens:
    print(alien)

print('___________________________')
print(f"total number of aliens is {len(aliens)}")