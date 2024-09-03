# using range to print the list item in index 2 and 4
""" names = ["tobi", "tayo", "segun", "daniel"]
for i in range(2, 4):
    print(names[i]) """

# printing the first 99 numbers starting from 0
""" for nums in range(100):
    print(nums) """

""" printing a range of numbers 
from 1 to 10 but stop printing when it is 4 
"""
""" for i in range(1, 10):
    print(i)
    if(i == 4):
        break """

# converts a range of number to list
# This method is known as typecasting
""" ages = list(range(18, 40))

for i in ages:
    if(i == 39):
        pass
    else:
        print(i, end=" || ") """

# using simple statistics method on numbers
""" digits = [4, 7, 7, 89, 0, 1, 89.3, 5, -0.5, 67]
print(min(digits))
print(sum(digits))
print(max(digits)) """

# List Comprehension
# var_name = [action for_loop]

squares = [num**2 for num in range(1, 11)]
print(squares)