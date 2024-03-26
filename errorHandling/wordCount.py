path = 'errorHandling/pythonpath.txt'

with open(path) as f:
    toCount = f.read()

counted = toCount.split()
length_of_file = len(counted)

print(f"there are {length_of_file}-words in the file")