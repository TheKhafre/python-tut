age = int(input("please enter your age: "))

if age <= 18 and age > 10:
    if age == 16:
        print("hey ! sweet 16")
    print("you're too young")
elif age >= 100 or age == 98:
    print("you're too old")
else:
    print("you have the perfect age")

print("bye for now")