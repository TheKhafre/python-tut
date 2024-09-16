# using flag to handle active and inactive state

""" active = True
while active:
    message = input("say something let me echo it back: ")

    if message == 'quit':
        active = False
    else:
        print(message) """

# Using a control statement to handle states
while True:
    message = input("say something let me echo it back: ")

    if message == 'quit':
        break
    else:
        print(message)