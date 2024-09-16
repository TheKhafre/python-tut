user = input("what's your name? "
             "I need to know who i'm dealing with."
             "Now, talk! who are you? ")

if user.lower() == 'tobi': #there is difference btw 'tobi' and 'Tobi'
    print('welcome back admin')
else:
    print('who the fuck are you?')

print(type(user))