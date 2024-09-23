# None is a placeholder that evaluates to False
def fullName(first_name, last_name, middle_name=None):

    if middle_name:
        # This only executes to true if there is a middle name supplied
        print(f"hello {first_name} {middle_name} {last_name}")
    else:
        print("there is no provision for middle name")
        print(f"hello {first_name} {last_name}")

fullName("Samuel", "Ajayi")
fullName("Oluwatobiloba", "Olajide", "Ezekiel")