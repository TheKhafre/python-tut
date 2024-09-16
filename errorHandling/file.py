# name of file to read/write
filename = 'my_text.txt'

# opening in read mode
""" with open(filename, 'w') as f:
    f.write("hello word") """

#opening in append mode
# TODO: please node that this will not add a new line automatically
    # if you need a new line in the text, then you should explicitly add it.
with open(filename, 'a') as file_object:
    file_object.write("Hello again, Dear World")