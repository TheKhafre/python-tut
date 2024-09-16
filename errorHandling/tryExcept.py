print("give two numbers to divide: "
    "\nEnter 'q' to quit.")

while True:
    first_num = input("what to divide: ")
    if first_num == 'q':
        break
    second_num = input("what to divide: by: ")
    if second_num == 'q':
        break

    try:
        answer = int(first_num) / int(second_num)
        print(f"answer is: {answer}")
    except ZeroDivisionError as e:
        print(f"\t{e}")
        print("please enter an int value greater than 0")
    else:
        print(answer)
