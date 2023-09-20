#characters.py
import random

###############################################
##### This is the Combat Atributes Module #####
###############################################
class Character:
    def __init__(self, name, max_hp, attack):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.gold = 0
        self.level = 1
        self.experience = 0
        self.experience_needed = 100
        self.inventory = []
        self.abilities = {}

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def gain_gold(self, amount):
        self.gold += amount

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=120, attack=15)
        self.abilities = {
            "Sword Slash": {"damage_multiplier": 1.5, "hit_chance": 0.8},
            "Axe Swing": {"damage_multiplier": 1.8, "hit_chance": 0.6},
            "Viking Heal": {"heal_amount": 20, "hit_chance": 0.8}
        }
        # Additional attributes specific to the Warrior class

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=80, attack=10)
        self.abilities = {
            "Fireball": {"damage_multiplier": 2.0, "hit_chance": 0.5},
            "Ice Blast": {"damage_multiplier": 1.6, "hit_chance": 0.7},
            "Restore": {"heal_amount": 20, "hit_chance": 0.8}
        }
        # Additional attributes specific to the Mage class

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=100, attack=12)
        self.abilities = {
            "Arrow Shot": {"damage_multiplier": 1.8, "hit_chance": 0.6},
            "Crossbow Bolt": {"damage_multiplier": 2.0, "hit_chance": 0.5},
            "Druidic Prayer": {"heal_amount": 20, "hit_chance": 0.8}
        } 
        # Additional attributes specific to the Archer class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=100, attack=12)
        self.abilities = {
            "Dual Sword Slash": {"damage_multiplier": 1.8, "hit_chance": 0.6},
            "Shadow Dance": {"damage_multiplier": 2.0, "hit_chance": 0.5},
            "Shadow Heal": {"heal_amount": 20, "hit_chance": 0.8}
        }
# Additional attributes specific to the Rogue class

class DarkKnight(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=100, attack=12)
        self.abilities = {
            "Longsword Slash": {"damage_multiplier": 1.8, "hit_chance": 0.6},
            "Blood Fountain": {"damage_multiplier": 2.0, "hit_chance": 0.5},
            "Dark Heal": {"heal_amount": 20, "hit_chance": 0.8}
        }
# Additional attributes specific to the DarkKnight class

class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=100, attack=12)
        self.abilities = {
            "Raise The Dead": {"damage_multiplier": 1.8, "hit_chance": 0.6},
            "Bone Collasol": {"damage_multiplier": 2.0, "hit_chance": 0.5},
            "Viking Heal": {"heal_amount": 20, "hit_chance": 0.8}
        }
# Additional attributes specific to the Necromancer class
class Agent(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=999, attack=999)
        self.abilities = {
            "Longsword Slash": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Dual Sword Slash": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Arrow Shot": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Sword Slash": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Axe Swing": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Crossbow Bolt": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Fireball": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Bone Collasol": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Ice Blast": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Raise The Dead": {"damage_multiplier": 50.0, "hit_chance": 1.0},
            "Shadow Dance": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Blood Fountain": {"damage_multiplier": 5.0, "hit_chance": 1.0},
            "Viking Heal": {"heal_amount": 500, "hit_chance": 1.0},
            "Dark Heal": {"heal_amount": 500, "hit_chance": 1.0},
            "Shadow Heal": {"heal_amount": 500, "hit_chance": 1.0},
            "Druidic Prayer": {"heal_amount": 500, "hit_chance": 1.0},
            "Restore": {"heal_amount": 500, "hit_chance": 1.0},
            "Viking Heal": {"heal_amount": 500, "hit_chance": 1.0}
        }
# Additional attributes specific to the hidden Agent class
###############################################
##### This is the Combat Atributes Module #####
###############################################

class Player(Character):
    def __init__(self, name, max_hp, attack, gold, character_class):
        super().__init__(name, max_hp, attack)
        self.gold = gold
        self.character_class = character_class
        self.abilities = {
            "Basic Attack": {"damage_multiplier": 1.0, "hit_chance": 1.0},
            "Special Attack": {"damage_multiplier": 1.5, "hit_chance": 0.8}
        }
        self.level = 1
        self.experience = 0
        self.experience_needed = 100
        self.inventory = []  # Inventory to store items

        # Customize abilities and other attributes based on character class
        if self.character_class == "Warrior":
            self.abilities.update({
                "Sword Slash": {"damage_multiplier": 1.5, "hit_chance": 0.8},
                "Axe Swing": {"damage_multiplier": 1.8, "hit_chance": 0.6},
                "Viking Heal": {"heal_amount": 20, "hit_chance": 0.8}
            })
            # Additional attributes specific to the Warrior class
        elif self.character_class == "Mage":
            self.abilities.update({
                "Fireball": {"damage_multiplier": 2.0, "hit_chance": 0.5},
                "Ice Blast": {"damage_multiplier": 1.6, "hit_chance": 0.7},
                "Restore": {"heal_amount": 20, "hit_chance": 0.8}
            })
            # Additional attributes specific to the Mage class
        elif self.character_class == "Archer":
            self.abilities.update({
                "Arrow Shot": {"damage_multiplier": 1.8, "hit_chance": 0.6},
                "Crossbow Bolt": {"damage_multiplier": 2.0, "hit_chance": 0.5},
                "Druidic Prayer": {"heal_amount": 20, "hit_chance": 0.8}
            })
            # Additional attributes specific to the Archer class
            
        elif self.character_class == "Rogue":
            self.abilities.update({
                "Dual Sword Slash": {"damage_multiplier": 1.8, "hit_chance": 0.6},
                "Shadow Dance": {"damage_multiplier": 2.0, "hit_chance": 0.5},
                "Shadow Heal": {"heal_amount": 20, "hit_chance": 0.8}
            })
            # Additional attributes specific to the Rogue class
        elif self.character_class == "DarkKnight":
            self.abilities.update({
                "Longsword Slash": {"damage_multiplier": 1.8, "hit_chance": 0.6},
                "Blood Fountain": {"damage_multiplier": 2.0, "hit_chance": 0.5},
                "Dark Heal": {"heal_amount": 20, "hit_chance": 0.8}
            })
    
            # Additional attributes specific to the Dark Knight class

        elif self.character_class == "Necromancer":
            self.abilities = {
                "Raise The Dead": {"damage_multiplier": 1.8, "hit_chance": 0.6},
                "Bone Collasal": {"damage_multiplier": 2.0, "hit_chance": 0.5},
                "Strength of The Dead": {"heal_amount": 20, "hit_chance": 0.8}
            }
        elif self.character_class == "Agent":
            self.abilities = {
                "Longsword Slash": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Dual Sword Slash": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Arrow Shot": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Sword Slash": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Axe Swing": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Crossbow Bolt": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Fireball": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Bone Collasol": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Ice Blast": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Raise The Dead": {"damage_multiplier": 50.0, "hit_chance": 1.0},
                "Shadow Dance": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Blood Fountain": {"damage_multiplier": 5.0, "hit_chance": 1.0},
                "Viking Heal": {"heal_amount": 500, "hit_chance": 1.0},
                "Dark Heal": {"heal_amount": 500, "hit_chance": 1.0},
                "Shadow Heal": {"heal_amount": 500, "hit_chance": 1.0},
                "Druidic Prayer": {"heal_amount": 500, "hit_chance": 1.0},
                "Restore": {"heal_amount": 500, "hit_chance": 1.0},
                "Viking Heal": {"heal_amount": 500, "hit_chance": 1.0}
            }
    
    def equip_item(self, item):
        if item in self.inventory:
            if "equipable" in item and item["equipable"]:
                # Check if the item is equipable
                if "equipped" not in item or not item["equipped"]:
                    # Check if the item is not already equipped
                    if "stat_bonus" in item:
                        stat_bonus = item["stat_bonus"]
                        # Apply the stat bonus to the player's attributes
                        for stat, value in stat_bonus.items():
                            setattr(self, stat, getattr(self, stat) + value)
                    item["equipped"] = True
                    print(f"You've equipped {item['name']}.")
                else:
                    print("Item is already equipped.")
            else:
                print("You can't equip this item.")
        else:
            print("Item not found in inventory.")

    def unequip_item(self, item):
        if item in self.inventory:
            if "equipable" in item and item["equipable"]:
                # Check if the item is equipable
                if "equipped" in item and item["equipped"]:
                    # Check if the item is currently equipped
                    if "stat_bonus" in item:
                        stat_bonus = item["stat_bonus"]
                        # Remove the stat bonus from the player's attributes
                        for stat, value in stat_bonus.items():
                            setattr(self, stat, getattr(self, stat) - value)
                    item["equipped"] = False
                    print(f"You've unequipped {item['name']}.")
                else:
                    print("Item is not currently equipped.")
            else:
                print("You can't equip this item.")
        else:
            print("Item not found in inventory.")

    def use_item(self, item, target=None):
        if item in self.inventory:
            if "usable" in item and item["usable"]:
                # Check if the item is usable
                if "consumable" in item and item["consumable"]:
                    # Check if the item is consumable
                    if "effect" in item:
                        effect = item["effect"]
                        if target and isinstance(target, Character):
                            if effect == "heal":
                                heal_amount = item["heal_amount"]
                                target.heal(heal_amount)
                                print(f"You've used {item['name']} on {target.name} and healed them for {heal_amount} HP.")
                                self.inventory.remove(item)
                            # Add more effects here as needed
                            else:
                                print("Invalid item effect.")
                        else:
                            print("Invalid target for item.")
                    else:
                        print("Item effect not defined.")
                else:
                    print("You can't use this item.")
            else:
                print("You can't use this item.")
        else:
            print("Item not found in inventory.")

    def use_ability(self, target):
        print("Abilities:")
        abilities = list(self.abilities.keys())
        
        for i, ability in enumerate(abilities, start=1):
            print(f"{i}. {ability}")

        choice = input("Choose an ability: ")

        if choice.isdigit():
            ability_index = int(choice) - 1

            if 0 <= ability_index < len(abilities):
                ability_name = abilities[ability_index]
                ability_details = self.abilities[ability_name]

                if "heal_amount" in ability_details:
                    heal_amount = ability_details["heal_amount"]
                    hit_chance = ability_details["hit_chance"]

                    if random.random() < hit_chance:
                        self.heal(heal_amount)
                        print(f"You use {ability_name} and heal yourself for {heal_amount} HP.")
                    else:
                        print(f"{ability_name} missed!")
                else:
                    damage_multiplier = ability_details["damage_multiplier"]
                    hit_chance = ability_details["hit_chance"]

                    if random.random() < hit_chance:
                        damage = int(self.attack * damage_multiplier)
                        target.take_damage(damage)
                        print(f"You use {ability_name} and deal {damage} damage to {target.name}.")
                    else:
                        print(f"{ability_name} missed!")
            else:
                print("Invalid ability choice.")
        else:
            print("Invalid input. Please enter a number corresponding to the ability.")


    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.experience_needed:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_needed
        self.experience_needed = int(self.experience_needed * 1.5)  # Increase the required experience for the next level
        self.max_hp += 10  # Customize the stat improvements for level-up
        self.attack += 2
        print(f"Congratulations! You've reached level {self.level}.")

    def apply_status_effects(self):
        pass

    def add_to_inventory(self, item):
        if len(self.inventory) < MAX_INVENTORY_SIZE:
            self.inventory.append(item)
        else:
            print("Inventory is full!")

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item not found in inventory!")

class Enemy(Character):
    def __init__(self, name, max_hp, attack, gold_reward, experience_reward):
        super().__init__(name, max_hp, attack)
        self.gold_reward = gold_reward
        self.experience_reward = experience_reward  # Add the experience_reward attribute
        self.status_effects = []

    def apply_status_effects(self):
        for effect in self.status_effects:
            self.take_damage(5)

    def add_status_effect(self, effect):
        self.status_effects.append(effect)

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, Attack: {self.attack}, Gold Reward: {self.gold_reward})"


# Define a constant for maximum inventory size
MAX_INVENTORY_SIZE = 10
# Define abilities separately outside of the Player class
ABILITIES = {
        "Basic Attack": {"damage_multiplier": 1.0, "hit_chance": 1.0},
        "Special Attack": {"damage_multiplier": 1.5, "hit_chance": 0.8}
}
