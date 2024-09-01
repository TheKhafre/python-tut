""" entry = ["taiwo", "bose", "Pelemo"]
for i in entry:
    print(i.title(), end=" | ") """

names = []

while True:
    print("to cancel, press q")
    response = input("please enter your name: ")

    if(response == 'q'):
        exit()

    names.append(response)
    print(names)