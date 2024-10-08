"""
    This opens a new file from the provided path
    and then print the content of the file
"""
with open('.\\fileHandling\\testfile.txt') as opened_file:
    content = opened_file.read()

print(content)