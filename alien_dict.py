alien_0 = {
    "x_pos": 0, 
    "y_pos": 25, 
    "speed": "medium"
}

# the .get takes 2 arguments: 
# the key to get its value, and
# the statement to return if that key does not exist
print(f"Original position: {alien_0.get('x_pos', 'x-pos doesnt exist')}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print(f"New position: {alien_0['x_pos']}")