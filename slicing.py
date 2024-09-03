""" players = ["daniel", "Feyi", "Fola", "Kemi", "Joseph"]
# to slice, the synthax is var_name[start:stop:step]
# the step is optional btw
# if we dont add start, it starts from 0
# if we dont add stop, it goes till the end of the list
# negative indexing counts from the back
print(players[1:3]) """

# looping through a list
""" players = ["daniel", "feyi", "fola", "kemi", "joseph"]

print("the last 3 names are:")
for player in players[-3:]:
    print(player.title()) """

# Copying List
players = ["Fola", "Kemi", "Joseph"]

other_players = players[:]
other_players.append("Khafre")

print(players)
print(other_players)

print("my players are:")
for player in players:
    print(player)

print("my friend's players are:")
for player in other_players:
    print(player)