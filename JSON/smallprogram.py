import json

def hello_user():
    filename = "new_user.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("what is your name: ").strip()

        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"your username has been saved as '{username}'")
    else:
        print(f"hello {username}, it's nice to have you back!")


hello_user()