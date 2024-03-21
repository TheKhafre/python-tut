usernames = [
    #"samuel",
    #"edo",
    #"tobi",
    #"admin",
    #"eros"
]

if usernames: # true only if there is atleast one element in the list
    for name in usernames:
        if name == "admin":
            print(f"\nHello {name.title()}, \n\twould you like a status report?")

        else:
            print(f"\nHello {name.title()}, thank you for logging in again")
else:
    print("We need to find some users!")
