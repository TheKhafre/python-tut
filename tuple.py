restaurant = ("rice", "beans", "spaghetti", "potato", "yam")

print("The food we serve includes: ")
for food in restaurant:
    if(food == "yam"):
        print(f"and {food}")
    else:
        print(food)