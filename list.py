# List is a collection of items arranged in a specific way
#accessing the elemnts of a list uses what is known as INDEX
# index refers to the position of an item.
# indexes in programming starts from 0, hence,
# the first element in the list occupies the index 0

"""boys = ["daniel", "benjy", "tobi", "junior"]
 print(boys[0].title())
print() """

# we use loop to print all the items in a list
""" for boy in boys:
    print(boy.title()) """

# negative index on the contrary starts from -1
# negative indexes are used to count from the back
# to access the last item in the list we just need to pass -1 as our index

""" print()
boys = ["daniel", "benjy", "tobi", "junior"]
print(boys[-1].title()) """

# important list format to learn
""" boys.reverse()
boys.sort() # sorts the elements alphabetically
boys.append("element to append") # appends new elemnt at the end of list
boys.copy() # copy the list to another variable
boys.insert(index, element_to_append)
boys.remove(element_to_remove) # removes element from list
boys.clear() # does not take arg. deletes everything in the list
boys.count("element to count") # used with print, this will return times the element appears
boys.index("element to search") # used with print, this returns the element's index
boys.pop(index) # deletes the element at the index """

# new_boys = boys.copy()
#boys.append("gbenga")

# print(new_boys)

foods = [] # instantiates an empty list
iterator = int(input("how many items do you want to add: "))

for i in range(iterator):
    food = input("add a new food: ")
    foods.append(food)
    foods.sort()

print(foods)