import random
import os
import sys
from colorama import init, Fore
from pyfiglet import Figlet
from characters import Player, Enemy
from locations import Town, load_game
import story

# Define the generate_random_enemy function here
def generate_random_enemy(player_level):
    # Define your list of enemies here
    enemy_list = [
        # ... (enemy definitions remain the same)
    ]
    
    # Generate a random index to select an enemy from the list
    random_index = random.randint(0, len(enemy_list) - 1)
    
    # Return the randomly selected enemy
    return enemy_list[random_index]

# Initialize colorama for colored output
init(autoreset=True)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Create a custom banner using pyfiglet
banner = Figlet(font='epic')
print(Fore.MAGENTA + banner.renderText("Enchanted Fantasy"))

# Define a function to add spacing and separators to text
def format_text(text):
    return f"\n{'*' * 50}\n{text}\n{'*' * 50}\n"

def starting_menu():
    print("Starting Menu:")
    print("1. New Game")
    print("2. Load Game")
    print("3. Settings")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_character()
    elif choice == "2":
        player = Player("", 0, 0, 0, "")  # Create a new player object with default values
        load_game(player)  # Call the load_game function
    elif choice == "3":
        # Settings logic here
        print("Settings:")
        print("1. Settings")
        print("2. Will")
        print("3. Go")
        print("4. Here")
        setting_choice = input("Enter your choice: ")
        if setting_choice == "1":
            sys.exit()
        elif setting_choice == "2":
            sys.exit()
        elif setting_choice == "3":
            sys.exit()
        elif setting_choice == "4":
            sys.exit()
    elif choice == "4":
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        starting_menu()

def create_character():
    # Get the player's name
    player_name = input("Enter your character's name: ")

    # Select character class
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Rogue")
    print("5. Dark Knight")
    print("6. Necromancer")

    class_choice = input("Enter the number of your choice: ")

    character_classes = {
        "1": "Warrior",
        "2": "Mage",
        "3": "Archer",
        "4": "Rogue",
        "5": "Dark Knight",
        "6": "Necromancer"
    }

    character_class = character_classes.get(class_choice, "Warrior")  # Default to Warrior if choice is invalid

    player = Player(player_name, 100, 10, 0, character_class)  # Pass the character_class parameter
    town = Town(character_class)

    while True:
        print(format_text("Delve Into The Void:"))
        print("1. Dungeons")
        print("2. Trials")
        print("3. Tower of Doom")
        print("4. Visit Town")
        print("5. Check Bag")
        print("6. Quit")

        choice = input("Enter your choice: ")
        print(f"____________________________")

        if choice == "1":
            print(format_text("You enter a dark and eerie dungeon."))
            print(format_text(story.generate_story()))
            random_enemy = generate_random_enemy(player.level)
            combat(player, random_enemy)
        elif choice == "2":
            print(format_text("You step into the challenging Trials."))
            random_enemy = generate_random_enemy(player.level + 1)  # Increase enemy difficulty for Trials
            combat(player, random_enemy)
        elif choice == "3":
            print(format_text("You enter the ominous Tower of Doom."))
            for floor in range(1, 11):  # Fight about 10 enemies on each floor
                random_enemy = generate_random_enemy(player.level + floor)  # Increase enemy difficulty with each floor
                print(f"Floor {floor}")
                combat(player, random_enemy)
                if not player.is_alive():
                    break  # End Tower of Doom if the player is defeated
        elif choice == "4":
            print(format_text("You visit the bustling town."))
            town.visit(player)
        elif choice == "5":
            print(format_text("You Check Your Bag!"))
            player.check_bag()
        elif choice == "6":
            print(format_text("Thanks for playing Enchanted Fantasy!"))
            break
        else:
            print("Invalid choice. Please try again.")

# Update the combat function to include a "Run" option
def combat(player, enemy):
    print(f"________________________________")
    print(f"A wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        # Print player and enemy health with colored text
        print(f"{Fore.GREEN}Player HP: {player.hp}/{player.max_hp}{Fore.RESET} | {Fore.RED}Enemy HP: {enemy.hp}/{enemy.max_hp}{Fore.RESET} | Class: {player.character_class}")
        print(f"Player Level: {player.level} | {Fore.YELLOW}Player Experience: {player.experience}/{player.experience_needed}{Fore.RESET}")
        print(f"______________________________________________")
        print("\nOptions:")
        print("1. Attack")
        print("2. Use Ability")
        print("3. Use Item")
        print("4. Check Bag")
        print("5. Run")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Roll a d20 for the player's attack
            player_attack_roll = random.randint(1, 20)
            if player_attack_roll >= 11:  # Adjust the threshold as needed
                player_attack = random.randint(1, player.attack)
                enemy.take_damage(player_attack)
                print(f"You attack the {enemy.name} for {player_attack} damage.")
            else:
                print("Your attack misses!")

        elif choice == "2":
            player.use_ability(enemy)
        
        elif choice == "3":
            player.use_ability(enemy)
        
        elif choice == "4":
            print(format_text("You Check Your Bag."))
            player.check_bag()  # Call the method to check the bag

        elif choice == "5":
            print("You attempt to run from the enemy.")
            if random.random() < 0.5:  # Adjust the run success chance as needed
                print("You successfully escape from the enemy!")
                break
            else:
                print("You failed to escape and must continue the battle.")

        else:
            print("Invalid choice. Please try again.")
            
        if enemy.is_alive():
            # Roll a d20 for the enemy's attack
            enemy_attack_roll = random.randint(1, 20)
            if enemy_attack_roll >= 11:  # Adjust the threshold as needed
                enemy_attack = random.randint(1, enemy.attack)
                player.take_damage(enemy_attack)
                print(f"The {enemy.name} attacks you for {enemy_attack} damage.")
            else:
                print(f"The {enemy.name}'s attack misses!")

        player.apply_status_effects()
        enemy.apply_status_effects()

    if player.is_alive():
        print(f"You defeated the {enemy.name}!")
        player.gain_gold(enemy.gold_reward)
        player.gain_experience(enemy.experience_reward)
    else:
        print("Game over. You were defeated.")

if __name__ == "__main__":
    starting_menu()