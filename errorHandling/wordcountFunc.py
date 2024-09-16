def wordCount(filename):
    try:
        with open(filename) as f:
            toCount = f.read()
    except FileNotFoundError:
        print(f"the file '{filename[:-4]}' does not exist")
    else:
        splitted = toCount.split()
        counted = len(splitted)

        print(f"there are {counted}-words in {filename[:-4]}")

path = "pythonpath.txt"
wordCount(path)