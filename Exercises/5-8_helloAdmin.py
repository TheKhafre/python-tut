Usernames = ['Samuel', 'Feyi', 'Admin', 'Tobi', 'Femi']

if Usernames:
    for user in Usernames:
        if user == 'Admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")

else:
    print("We need to find some users!")