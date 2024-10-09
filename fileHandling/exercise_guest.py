name = input("Please enter your name: ")

with open('myWrite.txt', 'a') as openFile:
    openFile.write(f"\n {name}")