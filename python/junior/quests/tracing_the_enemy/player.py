# Player module - Manages player state like health, keys, and position.

# Creative Instructions:
# Your Hero’s Fate: Guide your player through the dungeon, ensuring they stay healthy and collect keys.
# 1 - The player’s health, keys, and position must be tracked as they venture deeper.
# 2 - As the player faces challenges, they should collect keys and move through the dungeon.
# 3 - Be wary of global variables! Your hero’s journey is more stable when their data is neatly contained.

# Technical Instructions:
# Goal: Track the player's health, keys, and position accurately.
# 1 - Create a system where the player's state can be updated as they move through rooms and interact with the dungeon.
# 2 - Implement functionality for updating health, collecting keys, and moving rooms.
# 3 - Eliminate the use of global variables by encapsulating the player’s state into a class or another structured format.

health = 100  # Global variable for player's health
keys = 0      # Global variable for player's keys
position = 1  # Room number where the player starts

def update_health(amount):
    global health
    health += amount
    print(f"Health updated to: {health}")

def collect_key():
    global keys
    keys += 1
    print(f"Collected a key! You now have {keys} keys.")

def move_to_next_room():
    global position
    position += 1
    print(f"Moved to room {position}")
