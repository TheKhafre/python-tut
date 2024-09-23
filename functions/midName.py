def fullName(first_name, last_name, middle_name=''):

    if middle_name:
        print(f"hello {first_name} {middle_name} {last_name}")
    else:
        print("there is no provision for middle name")
        print(f"hello {first_name} {last_name}")

fullName("Samuel", "Ajayi")
fullName("Oluwatobiloba", "Olajide", "Ezekiel")