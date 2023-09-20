# player2.py

from characters import Character, MAX_INVENTORY_SIZE, ABILITIES

class Player2(Character):
    def __init__(self, name, max_hp, attack, gold, character_class):
        super().__init__(name, max_hp, attack)
        self.gold = gold
        self.character_class = character_class
        self.abilities = ABILITIES  # Use the same abilities as Player
        self.level = 1
        self.experience = 0
        self.experience_needed = 100
        self.inventory = []  # Inventory to store items

        # Customize abilities and other attributes based on character class
        if self.character_class == "Necromancer":
            self.abilities = {
                "Raise The Dead": {"damage_multiplier": 1.8, "hit_chance": 0.6},
                "Bone Collasal": {"damage_multiplier": 2.0, "hit_chance": 0.5},
                "Strength of The Dead": {"heal_amount": 20, "hit_chance": 0.8}
            }
            # Additional attributes specific to the Necromancer class
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
            # Additional attributes specific to the Agent class
        # Add more character class customizations as needed