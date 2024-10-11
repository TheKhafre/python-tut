from fileinput import filename


def word_count(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError as e:
        with open('missing.txt', 'a') as file:
            file.write(f"{filename} does not exist.\n")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"There are {num_words} words in {filename}.")

filename = ['.\\fileHandling\\testfile.txt', '.\\fileHandling\\fencefile.txt', '.\\fileHandling\\file_2.txt', '.\\fileHandling\\file_3.txt']
for file in filename:
    """ if FileNotFoundError:
        with open(file, 'a') as file:
            file.write(f"{filename} does not exit.") """
    word_count(file)
    print()