path = 'errorHandling/pythonpath.txt'

with open(path) as f:
    toReplace = f.readlines()

for line in toReplace:
    replaced = line.replace("python", "C") #replace all occurrence of python with C
    print(replaced.strip()) #removes unnecessary whitespace