import os
import pickle
from colorama import init, Fore
###################################
# This Is The section to add your #
#    Items, Potions, & Weapons    #
###################################

class Item:
    def __init__(self, name, description, gold_cost):
        self.name = name
        self.description = description
        self.gold_cost = gold_cost
        self.equipable = False  # Whether the item can be equipped
        self.equipped = False  # Whether the item is currently equipped
        self.usable = False  # Whether the item can be used
        self.consumable = False  # Whether the item is consumable
        self.effect = None  # The effect of the item (e.g., "heal", "damage", etc.)
        self.stat_bonus = {}  # A dictionary of stat bonuses (e.g., {"hp": 20, "attack": 10})

class Weapon(Item):
    def __init__(self, name, description, damage_bonus, gold_cost):
        super().__init__(name, description, gold_cost)
        self.damage_bonus = damage_bonus
        self.equipable = True  # Weapons are equipable
        self.usable = True  # Weapons can be used (e.g., for attacking)

class Potion(Item):
    def __init__(self, name, description, healing_amount, gold_cost):
        super().__init__(name, description, gold_cost)
        self.healing_amount = healing_amount
        self.usable = True  # Potions can be used
        self.consumable = True  # Potions are consumable
        self.effect = "heal"  # The effect of the potion is healing
        self.stat_bonus = {"hp": healing_amount}  # Potion provides an HP bonus

class Town:
    def __init__(self, character_class):
        self.bank_gold = 100

        if character_class == "Warrior":
            self.store_items = {
                "Potion": Potion("Potion", "Restores 20 HP", 20, 20),
                "Water": Potion("Water", "Restores 10 HP", 20, 20),
                "Elixer of Health": Potion("Elixer of Health", "Restores 400 HP", 400, 20),
                "Stone_Sword": Weapon("Stone Sword", "A basic sword", 10, 50),
                # Add Warrior-specific items here
            }
        elif character_class == "Mage":
            self.store_items = {
                "Potion": Potion("Potion", "Restores 20 HP", 20, 20),
                "Water": Potion("Water", "Restores 10 HP", 20, 20),
                "Elixer of Health": Potion("Elixer of Health", "Restores 400 HP", 400, 20),
                "Wand": Weapon("Wand", "A magical wand", 15, 60),
                # Add Mage-specific items here
            }
        elif character_class == "Archer":
            self.store_items = {
                "Potion": Potion("Potion", "Restores 20 HP", 20, 20),
                "Water": Potion("Water", "Restores 10 HP", 20, 20),
                "Elixer of Health": Potion("Elixer of Health", "Restores 400 HP", 400, 20),                
                "Bow": Weapon("Bow", "A sturdy bow", 12, 45),
                # Add Archer-specific items here
            }
        elif character_class == "Rogue":
            self.store_items = {
                "Potion": Potion("Potion", "Restores 20 HP", 20, 20),
                "Water": Potion("Water", "Restores 10 HP", 20, 20),
                "Elixer of Health": Potion("Elixer of Health", "Restores 400 HP", 400, 20),                
                "Dagger": Weapon("Dagger", "A Shiny Dagger", 12, 45),
                # Add Archer-specific items here
            }
        elif character_class == "DarkKnight":
            self.store_items = {
                "Potion": Potion("Potion", "Restores 20 HP", 20, 20),
                "Water": Potion("Water", "Restores 10 HP", 20, 20),
                "Elixer of Health": Potion("Elixer of Health", "Restores 400 HP", 400, 20),                
                "Long Sword": Weapon("Bow", "A Long Sword", 12, 45),
                # Add Archer-specific items here
            }
        elif character_class == "Necromancer":
            self.store_items = {
                "Potion": Potion("Potion", "Restores 20 HP", 20, 20),
                "Water": Potion("Water", "Restores 10 HP", 20, 20),
                "Elixer of Health": Potion("Elixer of Health", "Restores 400 HP", 400, 20),                
                "Staff": Weapon("Bow", "A Glowing Staff", 12, 45),
                # Add Archer-specific items here
            }
        elif character_class == "Agent":
            self.store_items = {
                "Potion": Potion("Potion", "Restores 20 HP", 20, 20),
                "Water": Potion("Water", "Restores 10 HP", 20, 20),
                "Elixer of Health": Potion("Elixer of Health", "Restores 400 HP", 400, 20),
                "God Stick": Weapon("God Stick", "A 1 Hit Menace", 1000, 1),                
                "Staff": Weapon("Staff", "A Glowing Staff", 12, 45),
                "Long Sword": Weapon("Long Sword", "A Long Sword", 12, 45),
                "Dagger": Weapon("Dagger", "A Shiny Dagger", 12, 45),
                "Bow": Weapon("Bow", "A sturdy bow", 12, 45),
                "Wand": Weapon("Wand", "A magical wand", 15, 60),
                "Stone_Sword": Weapon("Stone Sword", "A basic sword", 10, 50),
                # Add Agent-specific items here
            }

    def visit(self, player):
        print("You enter the town.")
        
        while True:
            print("\nOptions:")
            print("1. Visit Inn")  # New option to Visit The Inn
            print("2. Visit Bank")
            print("3. Visit General Store")
            print("4. Check Bag")  # New option to check the bag
            print("5. Leave Town")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.inn(player)
            elif choice == "2":
                self.bank(player)
            elif choice == "3":
                self.store(player)
            elif choice == "4":
                self.Check_Bag(player)
            elif choice == "5":
                print("You leave the town.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def check_bag(self, player):
        print("You check your bag.")
        # Display player's inventory
        print("Inventory:")
        for item in player.inventory:
            print(item)

    def bank(self, player):
        print(f"_______________________________")
        print(f"Bank gold: {Fore.YELLOW}{self.bank_gold}{Fore.RESET}")
        print(f"Your gold: {Fore.YELLOW}{player.gold}{Fore.RESET}")
        print(f"_______________________________")
        while True:
            print("\nOptions:")
            print("1. Deposit gold")
            print("2. Withdraw gold")
            print("3. Leave Bank")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                amount = int(input("Enter the amount to deposit: "))
                if player.gold >= amount:
                    player.gold -= amount
                    self.bank_gold += amount
                else:
                    print("You don't have enough gold.")
            elif choice == "2":
                amount = int(input("Enter the amount to withdraw: "))
                if self.bank_gold >= amount:
                    player.gold += amount
                    self.bank_gold -= amount
                else:
                    print("The bank doesn't have enough gold.")
            elif choice == "3":
                print("You leave the bank.")
                break
            else:
                print("Invalid choice. Please try again.")



    # Inn Function
    def inn(self, player):
        print("____________________________________________________________")
        print("Stepping inside the cozy inn, the gentle hum of conversation")
        print("Then the aroma of hearty meals instantly embraces you,")
        print("offering solace in the midst of your journey.")
        print("____________________________________________________________")
    
        while True:
            print("\nOptions:")
            print("1. Sleep The Night")
            print("2. Save Your Game")
            print("3. Load Your Game")
            print("4. Leave Inn")
        
            choice = input("Enter your choice: ")
        
            if choice == "1":
                print("You sleep for the night and feel refreshed and ready to go.")
                player.heal(player.max_hp - player.hp)  # Fully heal the character
            elif choice == "2":
                save_game(player)  # Call the save_game function
            elif choice == "3":
                load_game(player)  # Call the load_game function
            elif choice == "4":
                print("You leave the inn.")
                break
            else:
                print("Invalid choice. Please try again.")
              
    
    def store(self, player):
        print("Welcome to the General Store!")

        while True:
            print("\nOptions:")
            print("1. Buy Item")
            print("2. Sell Item")
            print("3. Leave Store")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Items for sale:")
                for item, item_object in self.store_items.items():
                    print(f"{item} - {item_object.description} - {item_object.name} - {item_object.healing_amount if isinstance(item_object, Potion) else item_object.damage_bonus} gold")

                item_choice = input("Enter the item you want to buy: ")

                if item_choice in self.store_items:
                    item_object = self.store_items[item_choice]
                    if player.gold >= item_object.gold_cost:
                        player.gold -= item_object.gold_cost
                        player.add_to_inventory(item_object)
                        print(f"You bought a {item_object.name}.")
                    else:
                        print("You don't have enough gold.")
                else:
                    print("Invalid item choice.")

            elif choice == "2":
                print("Items you can sell:")
                if not player.inventory:
                    print("Your inventory is empty.")
                else:
                    for index, item in enumerate(player.inventory, start=1):
                        print(f"{index}. {item.name}")

                    item_index = input("Enter the number of the item you want to sell (or '0' to cancel): ")
                    try:
                        item_index = int(item_index)
                        if item_index == 0:
                            continue
                        if 1 <= item_index <= len(player.inventory):
                            item_to_sell = player.inventory[item_index - 1]
                            player.gold += item_to_sell.gold_value
                            player.remove_from_inventory(item_to_sell)
                            print(f"You sold {item_to_sell.name} for {item_to_sell.gold_value} gold.")
                        else:
                            print("Invalid item index.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            elif choice == "3":
                print("You leave the store.")
                break
            else:
                print("Invalid choice. Please try again.")



# Define a directory to store saved games
SAVE_DIR = "saved_games"

# Create the save directory if it doesn't exist
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Function to load a saved game
def load_game(player):
    try:
        # Prompt the user to enter the name of the saved game file
        saved_game_name = input("Enter the name of the saved game: ")
        saved_game_path = os.path.join(SAVE_DIR, saved_game_name)

        if os.path.exists(saved_game_path):
            # Load the saved game data
            with open(saved_game_path, 'rb') as saved_game_file:
                loaded_data = pickle.load(saved_game_file)

            # Update the player's attributes with the loaded data
            player.__dict__.update(loaded_data)
            print("Game loaded successfully.")
        else:
            print("Saved game not found.")
    except Exception as e:
        print("An error occurred while loading the game:", str(e))

# Function to save the game
def save_game(player):
    try:
        # Prompt the user to enter a name for the saved game
        saved_game_name = input("Enter a name for the saved game: ")
        saved_game_path = os.path.join(SAVE_DIR, saved_game_name)

        # Create a dictionary with the player's attributes to be saved
        saved_data = player.__dict__

        # Save the game data using pickle
        with open(saved_game_path, 'wb') as saved_game_file:
            pickle.dump(saved_data, saved_game_file)

        print("Game saved successfully.")
    except Exception as e:
        print("An error occurred while saving the game:", str(e))