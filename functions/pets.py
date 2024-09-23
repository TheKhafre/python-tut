def describe_pet( pet_name, animal_type="cat"):
    print(f"I have a {animal_type.title()} named {pet_name.title()}")

# Positional Argument
describe_pet("nora", "dog")

# Keyword Argument
describe_pet(animal_type="dog", pet_name="nora")