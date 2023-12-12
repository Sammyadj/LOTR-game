"""
This class is the main class of the "Adventure World" application.
'Adventure World' is a very simple, text based adventure game. Users can walk
around some scenery. That's all. It should really be extended to make it more
interesting!

To play this game, create an instance of this class and call the "play" method.

This main class creates and initialises all the others: it creates all rooms,
creates the parser and starts the game. It also evaluates and executes the
commands that the parser returns.

This game is adapted from the 'World of Zuul' by Michael Kolling and 
David J. Barnes. The original was written in Java and has been simplified and
converted to Python by Kingsley Sage.
"""

from room import Room
from text_ui import TextUI
from backpack import Backpack
from player import Player


# New scenario-specific module
class LOTRGame:
    def __init__(self, player_name):
        self.create_locations()
        self.current_location = self.shire
        self.player = Player(player_name)
        self.text_ui = TextUI()

    def create_locations(self):
        self.shire = Room("in The Shire", items_quantities={"Hobbit Pipe": 3})
        self.rivendell = Room("in Rivendell", items_quantities={"Elven Bread":2, "Mithril Dagger":1})
        self.moria = Room("in the Mines of Moria", items_quantities={"Dwarf Helmet":2, "Dwarf Axe":1})
        self.mordor = Room("in Mordor", items_quantities={"One Ring":1})

        self.shire.set_exit("east", self.rivendell)
        self.rivendell.set_exit("west", self.shire)
        self.rivendell.set_exit("east", self.moria)
        self.moria.set_exit("west", self.rivendell)
        self.moria.set_exit("east", self.mordor)
        self.mordor.set_exit("west", self.moria)

    def play(self):
        self.print_welcome()
        finished = False
        while not finished:
            command = self.text_ui.get_command()
            finished = self.process_command(command)
        print("Thank you for playing!")

    def print_welcome(self):
        self.text_ui.print_to_textUI("Welcome to the world of The Lord of the Rings™.")
        self.text_ui.print_to_textUI("Your journey begins in The Shire.")
        self.text_ui.print_to_textUI(f'Your command words are: {self.show_command_words()}')
 


    def show_command_words(self):
        return ['help', 'go', 'quit', 'pickup', 'inventory']
    
    def do_view_command(self):
        description = self.current_location.get_long_description()
        items_description = self.current_location.get_items_description()
        self.text_ui.print_to_textUI(description)
        self.text_ui.print_to_textUI(items_description)
    

    def process_command(self, command):
        command_word, second_word = command
        if command_word is not None:
            command_word = command_word.upper()
    

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "GO":
            self.do_go_command(second_word)
        elif command_word == "QUIT":
            want_to_quit = True
        elif command_word == "PICKUP":
            self.do_pickup_command(second_word)
            self.do_view_command()
        elif command_word == "INVENTORY":
            self.do_inventory_command()
        elif command_word == "VIEW":  # New "VIEW" command
            self.do_view_command()
        else:
            self.text_ui.print_to_textUI("Don't know what you mean.")

        return want_to_quit
    

    def do_pickup_command(self, second_word):
        if second_word is not None:
            # Join all words after the command word to get the full item name (e.g. "one ring")
            item_to_pickup = ' '.join(second_word.split()).lower()

            item_names=list(self.current_location.item_quantities.keys())
            print('Debug test: ', item_names)
           

            # Check if the item is in the current location
            
            if item_to_pickup in [item.lower() for item in item_names]:
                # Capitalize the item name for display
                display_name = item_to_pickup.capitalize()
                print(f"DEBUG: Display name: {display_name}")

                if self.player.pickup_item(item_to_pickup, self.current_location):
                    self.text_ui.print_to_textUI(f"You picked up {display_name}.")
                    # Explicitly remove the item from the current_location.items list
                    self.current_location.remove_item(item_to_pickup)
                    self.current_location.items = list(self.current_location.item_quantities.keys())
                    if item_to_pickup == "one ring":  # Use lowercase version here as well
                        self.text_ui.print_to_textUI("Congratulations! You have completed your quest.")
                        return True 
                else:
                    self.text_ui.print_to_textUI("Your backpack is full. Drop something first.")
            else:
                self.text_ui.print_to_textUI(f"There is no {item_to_pickup} in this location.")
    

    def do_inventory_command(self):
        inventory = self.player.show_inventory()
        if inventory:
            self.text_ui.print_to_textUI("Your inventory:")
            for item in inventory:
                self.text_ui.print_to_textUI(f"- {item}")
        else:
            self.text_ui.print_to_textUI("Your inventory is empty.")
    

    def print_help(self):
        self.text_ui.print_to_textUI("Welcome to the world of The Lord of the Rings™.")
        self.text_ui.print_to_textUI("Your journey begins in The Shire.")
        self.text_ui.print_to_textUI(f'Your command words are: {self.show_command_words()}.')

    def do_go_command(self, second_word):
        if second_word is None:
            self.text_ui.print_to_textUI("Go where?")
            return

        next_location = self.current_location.get_exit(second_word)
        if next_location is None:
            self.text_ui.print_to_textUI("There is no path in that direction.")
        else:
            self.current_location = next_location
            self.text_ui.print_to_textUI(self.current_location.get_long_description())


def main():
    player_name = input("Enter your name: ")
    lotr_game = LOTRGame(player_name)
    lotr_game.play()


if __name__ == "__main__":
    main()
