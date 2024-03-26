import json

number = [1, 2, 3, 4, 5, 8, 90, 63]
filename = 'num.json'

with open(filename, 'w') as f:
    json.dump(number, f)