# Dungeon module - Manages the dungeon states, door, keys, enemies and etc.

# Creative Instructions:
# The Dungeon’s Secrets: Unlock the path forward by managing the dungeon’s traps and treasures.
# 1 - The dungeon holds locked doors and dangerous enemies; the player’s actions will affect their progress.
# 2 - Don’t let the keys and health be lost in the dungeon’s dark corners. Keep track of them as the hero interacts.
# 3 - The player's state must be communicated clearly as they encounter challenges—will they survive the dungeon’s wrath?

# Technical Instructions:
# Goal: Implement game mechanics for dungeon interactions that impact the player.
# 1 - Develop functions for opening doors and handling enemies. These actions should modify the player's state (keys, health).
# 2 - Ensure that when the player interacts with objects, their data (health, keys) is updated correctly.
# 3 - Properly pass the player object to functions in this module to maintain consistency and avoid unexpected results.

import player

def open_door():
    if player.keys > 0:
        player.keys -= 1
        print("Door opened!")
    else:
        print("You need a key to open this door!")

def encounter_enemy():
    if player.health > 0:
        print("An enemy appears!")
        player.update_health(-10)
    else:
        print("You have no health left!")
        print("Game Over!")
