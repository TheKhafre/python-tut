names = {
    1 : 'tobi',
    2 : 'femi',
    3 : 'daniel',
    4 : 'femi',
    5 : 'tobi'
}

#this converts the values to a set to print only unique values
#no repeated value; all values will be printed once
for name in set(names.values()):
    print(name)
print('\n')

# prints the dictionary in sorted arrangement
for name in sorted(names.values()):
    print(name)