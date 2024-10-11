"""
    This opens and read the file content line-by-line
"""

file_path = '.\\fileHandling\\testfile.txt'

""" with open(file_path) as opened_file:
    for line in opened_file:
        print(line.strip()) """

with open(file_path) as opened_file:
    # when we use read(), it tokenize by letter but
    # using readlines() tokenize by lines, saving each line to the assigned variable.
    lines = opened_file.read()

split_num = lines.split()
print(f"The file has {len(split_num)} words")
