
class NotInBackpackError(Exception):
    def __init__(self, item, message):
        print(f'{item} {message}')

class Backpack:
    """
    A class to allow us to pickup and put down items...
    Backpack is limited to number of items set by capacity.
    This example incorporates a user defined exception.
    """

    def __init__(self, capacity):
        self.contents = []
        self.capacity = capacity
        self.current_weight = 0

    def add_item(self, item,weight):
        """Adds an item to our backpack."""
        if self.current_weight + weight <= self.capacity:
            self.contents.append(item)
            self.current_weight += weight
            return True
        return False

    def remove_item(self, item, weight):
        """Removes an item from our backpack."""
        try:
            if item not in self.contents:
                raise NotInBackpackError(item, 'is not in the backpack.')
            self.contents.remove(item)
            self.current_weight -= weight
        except NotInBackpackError:
            print('Exception handled here...')
        finally:
            print('Carrying on...')

    def check_item(self, item):
        """Returns True if item is in backpack, False otherwise."""
        return item in self.contents



# # class Backpack:
# #     def __init__(self, capacity):
# #         self.contents = []
# #         self.capacity = capacity
# #         self.current_weight = 0

# #     def add_item(self, item, weight):
# #         """Adds an item to our backpack."""
# #         if self.current_weight + weight <= self.capacity:
# #             self.contents.append(item)
# #             self.current_weight += weight
# #             return True
# #         return False

#     def remove_item(self, item, weight):
#         """Removes an item from our backpack."""
#         if item not in self.contents:
#             raise NotInBackpackError(item, 'is not in the backpack.')
#         self.contents.remove(item)
#         self.current_weight -= weight

#     def check_item(self, item):
#         return item in self.contents