import json

filename = "num.json"

with open(filename) as f:
    value = json.load(f)

print(value)