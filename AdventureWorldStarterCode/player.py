
from backpack import Backpack

'''
Player class for AdventureWorld game.
This class is responsible for keeping track of the player's name, backpack, and backpack capacity.

'''

class Player:
    def __init__(self, name, backpack_capacity=6):
        self.name = name
        self.backpack = Backpack(backpack_capacity)

    def pickup_item(self, item, current_room):
        '''
        Adds an item to the player's backpack.
        Returns True if the item was successfully added, False otherwise.
        '''
        item_weight = 1 # Assuming a default weight for items
        if self.backpack.add_item(item, item_weight):
            current_room.remove_item(item)
            return True
        else:
            return False

    def show_inventory(self): # Returns a list of items in the player's backpack.
        return self.backpack.contents 

