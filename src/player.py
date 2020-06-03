# Write a class to hold player information, e.g. what room they are in
# currently.
class player():
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None: self.current_room = getattr(self.current_room,f"{direction_to")
        else:
            print("They way is impassable!")