def spag_ingredient(pots, *extras):
    print(f"\nMaking {pots}-pots of Spaghetti with the following extras:")
    for extra in extras:
        print(f"- {extra}")

spag_ingredient(3, 'Chicken', 'beans', 'vegetable')
spag_ingredient(2, 'french fries')