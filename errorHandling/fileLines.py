myfile = "my_text.txt"

""" 'with open' is a statement that we can use to open
 and be sure it will close itself after operation """
with open(myfile) as file:
    text_lines = file.readlines()
    #text_lines = file.read()

""" Naturally when we use loop to print a readline object,
it comes with a weird newline added to it, to remove the new line,
we use the strip function that removes whitespaces left and right """
for line in text_lines:
    print(line.strip())

#print(len(text_lines.split()))