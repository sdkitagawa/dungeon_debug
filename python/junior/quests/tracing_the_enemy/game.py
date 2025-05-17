# Game module - Controls the flow of the game.

# Creative Instructions:
# The Dungeon Master’s Challenge: Guide your hero through the perilous dungeon.
# 1 - Lead your player through a series of rooms—collecting keys, unlocking doors, and avoiding death.
# 2 - Keep the game moving, but remember, tracking the hero’s health and progress is key to their survival.
# 3 - Trace the hero’s journey and ensure that every decision—whether a key collected or health lost—is visible in the game’s flow.

# Technical Instructions:
# Goal: Control the flow of the game and track the player's progress through the dungeon.
# 1 - Manage the sequence of rooms the player moves through, ensuring keys are collected and doors are unlocked.
# 2 - Ensure that the game consistently updates and displays the player's current state (health, keys, position).
# 3 - Debug the flow of the game so that the player's progress is logical and traceable, with no data inconsistencies.

import player
import dungeon

def start_game():
    print("Welcome to the Dungeon!")
    while player.health > 0 and player.position <= 5:
        print(f"\nYou are in room {player.position}")
        
        if player.position == 2:
            print("You found a key!")
            player.collect_key()
        
        if player.position == 3:
            print("There is a locked door.")
            dungeon.open_door()
        
        if player.position == 4:
            print("An enemy appears!")
            dungeon.encounter_enemy()
        
        if player.position == 5:
            print("You reach the final room! Congratulations!")
            break
        
        player.move_to_next_room()

def main():
    start_game()

if __name__ == "__main__":
    main()
