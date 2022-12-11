from Dungeon import Dungeon
from Adventurer import Adventurer

def DungeonAdventure():
  """
  DungeonAdventure:

  A function containing the main logic for playing the game and
    • introduces the game describing what the game is about and how to play
    • Creates a Dungeon Object and an Adventurer Object
    • Obtains the name of the adventurer from the user
    • Does the following repetitively:
        o Prints the current room (this is based on the Adventurer's current location)
        o Determines the Adventurer's options (Move, Use a Potion)
        o Continues this process until the Adventurer wins or dies
    • At the conclusion of the game, displays the entire Dungeon
  """
  valid = False
  dungeon = None
  while not valid:
    dungeon = Dungeon(5, 5)
    if dungeon.traverse(0, 0):
      print("Valid dungeon created!")
      valid = True
    else:
      print("exit not reachable, making a new dungeon...")

  print("\nWhy hello there stranger! Let's play a dungeon adventure game!\n")

  user_name = input("Your name is: ")
  adventurer = Adventurer(user_name)

  print(f"Welcome, {user_name}!\n\nYour goal is to find the four Pillars of Object Oriented Programming (Abstraction, Encapsulation, Inheritance, and Polymorphism) and take them to the dungeon's exit to win the game.")
  print(f"\nSome features of the dungeon will prove a hindrance to {user_name}'s task, such as dangerous spiked pits!\nSome items will prove helpful on your journey, such as healing potions which replenish some HP and vision potions that allow you to temporarily see more of the map.")

  print("\nMap Legend:\n- 'i': Entrance of the Dungeon\n- 'O': Exit of the Dungeon\n- 'H': Health Potion\n- 'V': Vision Potion\n- 'M': Multiple Potions\n- 'X': Pit\n- 'P': Polymorphism Pillar\n- 'A': Abstraction Pillar\n- 'E': Encapsulation Pillar\n- 'I': Inheritance Pillar\n")

  print(f"You are starting the game with {adventurer.hit_points} HP\n")

  while adventurer.alive:
    print(f"{adventurer.name} is at {adventurer.x}, {adventurer.y}")
    north_room, south_room, west_room, east_room = adventurer.available_rooms(dungeon)

    if adventurer.enhanced_vision:
      blank_string = "     \n     \n     \n"

      north = dungeon.draw_room_by_coord(adventurer.x, adventurer.y - 1) if dungeon.draw_room_by_coord(adventurer.x, adventurer.y - 1) is not None else blank_string
      nw = dungeon.draw_room_by_coord(adventurer.x - 1, adventurer.y - 1) if dungeon.draw_room_by_coord(adventurer.x - 1, adventurer.y - 1) is not None else blank_string
      ne = dungeon.draw_room_by_coord(adventurer.x + 1, adventurer.y - 1) if dungeon.draw_room_by_coord(adventurer.x + 1, adventurer.y - 1) is not None else blank_string

      south = dungeon.draw_room_by_coord(adventurer.x, adventurer.y + 1) if dungeon.draw_room_by_coord(adventurer.x, adventurer.y + 1) is not None else blank_string
      sw = dungeon.draw_room_by_coord(adventurer.x - 1, adventurer.y + 1) if dungeon.draw_room_by_coord(adventurer.x - 1, adventurer.y + 1) is not None else blank_string
      se = dungeon.draw_room_by_coord(adventurer.x + 1, adventurer.y + 1) if dungeon.draw_room_by_coord(adventurer.x + 1, adventurer.y + 1) is not None else blank_string

      east = dungeon.draw_room_by_coord(adventurer.x + 1, adventurer.y) if dungeon.draw_room_by_coord(adventurer.x + 1, adventurer.y) is not None else blank_string
      west = dungeon.draw_room_by_coord(adventurer.x - 1, adventurer.y) if dungeon.draw_room_by_coord(adventurer.x - 1, adventurer.y) is not None else blank_string

      center = dungeon.draw_room_by_coord(adventurer.x, adventurer.y)

      dungeon.print_room_rows([nw, north, ne])
      dungeon.print_room_rows([west, center, east])
      dungeon.print_room_rows([sw, south, se])
    else:
      print(dungeon.draw_room_by_coord(adventurer.x, adventurer.y))

    dungeon.clear_room(adventurer.x, adventurer.y)
    dungeon.clear_pillars(adventurer.x, adventurer.y)

    adventurer.move(north_room, south_room, west_room, east_room)


  print("===== fin =====")
  dungeon.print_maze_by_coords()

DungeonAdventure()

response = input("Would you like to play again? y/n\n").lower()

if response == "y":
  print("Starting a new game!...")
  DungeonAdventure()
elif response == "n":
  print("Thank you for playing!")