file_path = '.\\fileHandling\\testfile.txt'

with open(file_path) as opened_file:
    lines = opened_file.readlines()

for line in lines:
    # replace the occurence of World with Lagos
    print((line.replace('World', 'Lagos')).strip())