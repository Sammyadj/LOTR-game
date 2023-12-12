from text_ui import TextUI

"""
Create a room described "description". Initially, it has no exits. The
'description' is something like 'kitchen' or 'an open court yard'.
"""


class Room:

    def __init__(self, description,items_quantities=None, items=None):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.description = description
        self.exits = {}  # Dictionary
        # self.items = items if items else []
        self.item_quantities = items_quantities if items_quantities else {}  # Dictionary to store item quantities
        if items:
            for item in items:
                self.add_item(item)

    

    def add_item(self, item, quantity=1):
        # Add or update the quantity of an item in the room
        self.item_quantities[item.lower()] = self.item_quantities.get(item.lower(), 0) + quantity



    def remove_item(self, item, quantity=1):
        # Remove or update the quantity of an item in the room
        current_quantity = self.item_quantities.get(item.lower(), 0)
        if current_quantity >= quantity:
            self.item_quantities[item.lower()] = current_quantity - quantity

            # Remove the item key if the quantity becomes zero
            if self.item_quantities[item.lower()] == 0:
                del self.item_quantities[item.lower()]
        
        else:
            # Handle the case where the quantity is less than requested
            self.text_ui.print_to_textUI(f"There is not enough {item} in this location.")

        

    def set_exit(self, direction, neighbour):
        
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return self.description

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.get_exits()}.'

    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    # def get_items_description(self):
    #     """
    #     Fetch a description of items available in the room.
    #     :return: text description
    #     """
    #     # items_list = [f"{item.capitalize()} ({quantity})" for item, quantity in self.item_quantities.items()]
    #     # if items_list:
    #     #     return f'Items in this location: {", ".join(items_list)}.'
    #     # else:
    #     #     return 'No items in this location.'

    def get_items_description(self):
        """
        Fetch a description of items available in the room.
        :return: text description
        """
        if self.item_quantities:
            items_list = ", ".join([f"{item} ({quantity})" for item, quantity in self.item_quantities.items()])
            return f'Items in this location: {items_list}.'
        else:
            return 'No items in this location.'
