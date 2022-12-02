from Dungeon import Dungeon
from Adventurer import Adventurer
from Room import Room

class DungeonAdventure:
  """
  Contains the main logic for playing the game
    • Introduces the game describing what the game is about and how to play
    • Creates a Dungeon Object and a Adventurer Object
    • Obtains the name of the adventurer from the user
    • Does the following repetitively:
        o Prints the current room (this is based on the Adventurer's current location)
        o Determines the Adventurer's options (Move, Use a Potion)
        o Continues this process until the Adventurer wins or dies
        o NOTE: Include a hidden menu option for testing that prints out the entire Dungeon -- specify what the menu option
        is in your documentation for the DungeonAdventure class
    • At the conclusion of the game, display the entire Dungeon
  """

  print("Why hello there stranger! Let's play a dungeon adventure game!")
  print("[Introduces the game describing what the game is about and how to play]\n")

  # Obtains the name of the adventurer from the user
  new_player = input("What will be the name of your brave adventurer?\n")

  # Create a new Dungeon
  # dungeon = Dungeon()

  # Create a new Adventurer
  adventurer = Adventurer(new_player)

  print(f"\nHello, {adventurer.name}! You are starting the game with {adventurer.hit_points} HP")

  # Some infinite while loop until the player wins or dies
  # while True:
    # print room
    # move, use item, or view player status

  adventurer.move()


DungeonAdventure()
