"""
    This opens a new file from the provided path
    and then print the content of the file.

    PS: the file needs to be opeend as something
        because to read the content, we need something to call.

    in this example, we opened as 'opened_file' and save in the variable 'content'.
"""

file_path = '.\\fileHandling\\testfile.txt'

with open(file_path) as opened_file:
    content = opened_file.read()

""" with open('.\\fileHandling\\testfile.txt') as opened_file:
    content = opened_file.read() """

print(content)