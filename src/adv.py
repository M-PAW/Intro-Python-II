import textwrap

from room import Room
from player import Player
from item import Item

# Declare all items

item = {
    'rusty dagger': Item('rusty dagger', "A chipped rusty old dagger."),
    'broken sword': Item('broken sword', "A reminent of a vicious fight."),
    'mysterious key': Item('mysterious key', "A key to either great treasure or peril."),
    'musty cloak': Item('musty cloak', "It smells like something died!"),
    'valyrian steel sword': Item('valerian steel sword', "On the sword is engraved the Longclaw.")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False, [item['broken sword']], [item['rusty dagger']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False, [item['mysterious key']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False, [item['musty cloak']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False, [item['valyrian steel sword']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link items to rooms
room['']
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Greeting! What is your name? ')
new_player = Player(name, current_room = room['outside'])

# Write a loop that:
#
while True:
    print(f'\n{new_player.player_name} has arrived -> {new_player.current_room}\n')
 

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# 
    command = input("\nWhich direction? ").lower()
    if command == "q":
        print(f'\nFarewell, {new_player.player_name}!')
        exit()
    elif command == "n":
        if new_player.current_room.n_to is not None:
            new_player.current_room = new_player.current_room.n_to
        else:
            print("There is no safe passage!")

    elif command == "s":
        if new_player.current_room.s_to is not None:
            new_player.current_room = new_player.current_room.s_to
        else:
            print("There is no safe passage!")

    elif command == "e":
        if new_player.current_room.e_to is not None:
            new_player.current_room = new_player.current_room.e_to
        else:
            print("There is no safe passage!")

    elif command == "w":
        if new_player.current_room.w_to is not None:
            new_player.current_room = new_player.current_room.w_to
        else:
            print("There is no safe passage!")

    else:
        print("\n I don't understand your command! \n")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
