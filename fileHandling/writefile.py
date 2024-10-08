file_path = '.\\fileHandling\\testfile.txt'

with open(file_path) as opened_file:
    lines = opened_file.readlines()

with open('myWrite.tx', 'w') as writeFile:
    for line in lines:
    # replace the occurence of World with Lagos
        writeFile.write(line)