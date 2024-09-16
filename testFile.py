""" entry = ["taiwo", "bose", "Pelemo"]
for i in entry:
    print(i.title(), end=" | ") """

names = []
print("to cancel, press q")

while True:
    response = input("please enter your name: ")

    if(response == 'q'):
        exit()

    names.append(response)
    
    if(len(names) > 4):
       # names.sort()
        print(f"The list contains")
        for i in names:
            print(i, end=" | ")
        print("\n")
    else:
        print(f"you just added {names[-1]} to the list")
        