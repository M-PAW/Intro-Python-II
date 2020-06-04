# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self,room_name, description, booled, **items):
        self.room_name = room_name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        result = f"{self.room_name}\n{self.description}\n"
        if self.n_to:
            result += f"N: {self.n_to.room_name}\n"
        if self.s_to:
            result += f"S: {self.s_to.room_name}\n"
        if self.e_to:
            result += f"E: {self.e_to.room_name}\n"
        if self.w_to:
            result += f"W: {self.w_to.room_name}\n"
        return result

    def get_item(self):
        if self.item == []:
            return f'This room has no items.'
        else:
            return f'Room items: {self.items}'