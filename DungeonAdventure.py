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

  # Create a new Adventurer
  adventurer = Adventurer(new_player)

  print(f"\nHello, {adventurer.name}! You are starting the game with {adventurer.hit_points} HP")

  # Infinite loop that runs until we have a valid, traversable Dungeon
  valid = False
  dungeon = None
  while not valid:
  # Create a new Dungeon
    dungeon = Dungeon(5, 5)
    # See if it's traversable, starting from 0,0
    if dungeon.traverse(0, 0):
      # if it IS, then set valid to True to exit the loop
      print("whoo hoo, we can reach the exit")
      valid = True
    else:
      # if it ISN'T, do the loop again and generate a new dungeon
      print("exit not reachable")

  # Some infinite while loop until the player wins or dies
  while adventurer.alive:
    print(f"{adventurer.name} is at {adventurer.x}, {adventurer.y}")

    # Where can we go?
    can_move_north = dungeon.get_room(adventurer.x, adventurer.y-1) is not None and dungeon.get_room(adventurer.x, adventurer.y-1).can_move_to()
    can_move_south = dungeon.get_room(adventurer.x, adventurer.y+1) is not None and dungeon.get_room(adventurer.x, adventurer.y+1).can_move_to()
    can_move_west = dungeon.get_room(adventurer.x-1, adventurer.y) is not None and dungeon.get_room(adventurer.x-1, adventurer.y).can_move_to()
    can_move_east = dungeon.get_room(adventurer.x+1, adventurer.y) is not None and dungeon.get_room(adventurer.x+1, adventurer.y).can_move_to()

    # SHOW THE ROOM
    room_content = str(dungeon.get_room(adventurer.x, adventurer.y))

    print("*-*") if can_move_north else print("***")

    if can_move_east and can_move_west:
      print(f"|{room_content}|")
    elif not can_move_east and can_move_west:
      print(f"|{room_content}*")
    elif can_move_east and not can_move_west:
      print(f"*{room_content}|")
    else:
      print(f"*{room_content}*")

    print("*-*") if can_move_south else print("***")

    # move, use item, or view player status
    adventurer.move()


DungeonAdventure()
