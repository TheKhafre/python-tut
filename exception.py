try:
    val_1 = int(input("enter a value for division: "))
    val_2 = int(input("enter a value to divide by: "))

    result = val_1 / val_2
except ValueError as e:
    print("you can only use a number")
    print(e)
except ZeroDivisionError as e:
    print("you cant divide by zero")
    print(e)
except Exception as e:
    print("something went wrong")
    print(e)

else:
    print(f"result is {result}")