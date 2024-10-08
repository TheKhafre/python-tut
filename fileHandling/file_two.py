"""
    This opens and read the file content line-by-line
"""

file_path = '.\\fileHandling\\testfile.txt'

with open(file_path) as opened_file:
    for line in opened_file:
        print(line.strip())
    