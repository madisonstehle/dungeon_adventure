import random

class Adventurer:
  """
  Adventurer Class:

  A class containing all attributes and methods pertaining to the Adventurer
  and their interaction with the world

  • Contains Attributes:
    o healing_potions: int
    o vision_potions: int
    o pillar_pieces_found: list of strings
    o cooldown: int

  • Contains Methods:
    o __init__
    o __str__
    o move
    o available_rooms
    o respond_to_room
    o hp_increase
    o hp_decrease
  """
  healing_potions = 1
  vision_potions = 1
  pillar_pieces_found = []
  cooldown = 3

  def __init__(self, name):
    """
    constructor __init__(self, name) that creates a new Adventurer object
      Attributes:
        - test_mode: boolean
        - name: user input string
        - hit_points: int
        - x (position as coordinate): int
        - y (position as coordinate): int
        - enhanced vision (if they have used a vision potion or not): boolean
        - alive: boolean

      parameters: name
      return: None
    """
    self.test_mode = False
    self.name = name
    self.hit_points = random.randint(75, 100)
    self.x = 0
    self.y = 0
    self.enhanced_vision = False
    self.alive = True

  def __str__(self):
    """
    __str__(self) method that builds a String containing:
      o Name
      o Hit Points
      o Total Healing Potions
      o Total Vision Potions
      o List of Pillars Pieces Found

      parameters: None
      return: String
    """
    pillars_string = ""

    if self.pillar_pieces_found:
      for pillar in self.pillar_pieces_found:
        if pillar is not self.pillar_pieces_found[len(self.pillar_pieces_found) - 1]:
          pillars_string += f"pillar {pillar}, "
        else:
          pillars_string += f"pillar {pillar}"
    else:
     pillars_string = "No pillars found yet!"

    return f"{self.name} has {self.hit_points} hp\nThey have collected:\n* {self.healing_potions} healing potions\n* {self.vision_potions} vision potions\n* {pillars_string}\n"

  def move(self, north_room, south_room, west_room, east_room):
    """
    move(self, north_room, south_room, west_room, east_room) method that contains logic for user moves
      parameters: north_room, south_room, west_room, east_room
      return: None
    """
    if self.enhanced_vision:
      self.cooldown -= 1
      if self.cooldown == 0:
        print("Your vision potion wore off!")
        self.enhanced_vision = False

    if self.test_mode:
      if self.healing_potions == 2:
        key = "h"
      else:
        key = "s"
    else:
      key=input(
        "a, w, s, d to move your adventurer | h to use healing potion | v to use vision potion | i to see adventurer information | q to quit\n").lower()

    match key:
      case "a":
        if west_room:
          print("moving west")
          self.x -= 1
          self.respond_to_room(west_room.get_room_content())
        else:
          print("You cannot move west!")
          self.move(north_room, south_room, west_room, east_room)
      case "w":
        if north_room:
          print("moving north")
          self.y -= 1
          self.respond_to_room(north_room.get_room_content())
        else:
          print("You cannot move north!")
          self.move(north_room, south_room, west_room, east_room)
      case "s":
        if south_room:
          print("moving south")
          self.y += 1
          self.respond_to_room(south_room.get_room_content())
        else:
          print("You cannot move south!")
          if self.test_mode:
            return
          else:
            self.move(north_room, south_room, west_room, east_room)
      case "d":
        if east_room:
          print("moving east")
          self.x += 1
          self.respond_to_room(east_room.get_room_content())
        else:
          print("You cannot move east!")
          self.move(north_room, south_room, west_room, east_room)
      case "h":
        if self.healing_potions != 0:
          self.hp_increase()
          print(f"You used a health potion! Your HP is now {self.hit_points}")
          self.healing_potions -= 1
        else:
          print("You don't have any healing potions!")
        self.move(north_room, south_room, west_room, east_room)
      case "v":
        if self.vision_potions != 0:
          self.enhanced_vision = True
          print("You used a vision potion! It lasts two turns.")
          self.vision_potions -= 1
          self.cooldown = 3
        else:
          print("You don't have any vision potions!")
          self.move(north_room, south_room, west_room, east_room)
      case "i":
        print(self.__str__())
        self.move(north_room, south_room, west_room, east_room)
      case "q":
        self.alive = False
      case _:
        self.move(north_room, south_room, west_room, east_room)

  def available_rooms(self, dungeon):
    """
    available_rooms(self, dungeon) method that determines which directions user can move
      parameters: dungeon
      return: Adjacent Room Objects
    """
    if dungeon.get_room(self.x, self.y - 1) is not None and dungeon.get_room(self.x, self.y - 1).can_move_to():
      north_room = dungeon.get_room(self.x, self.y - 1)
    else:
      north_room = None

    if dungeon.get_room(self.x, self.y + 1) is not None and dungeon.get_room(self.x, self.y + 1).can_move_to():
      south_room = dungeon.get_room(self.x, self.y + 1)
    else:
      south_room = None

    if dungeon.get_room(self.x - 1, self.y) is not None and dungeon.get_room(self.x - 1, self.y).can_move_to():
      west_room = dungeon.get_room(self.x - 1, self.y)
    else:
      west_room = None

    if dungeon.get_room(self.x + 1, self.y) is not None and dungeon.get_room(self.x + 1, self.y).can_move_to():
      east_room = dungeon.get_room(self.x + 1, self.y)
    else:
      east_room = None

    return north_room, south_room, west_room, east_room

  def respond_to_room(self, room_content):
    """
    respond_to_room(self, room_content) method that allows the adventurer to interact with what is in the new room
      parameters: room_content
      return: None
    """
    if room_content == "X":
      self.hp_decrease()
      print(f"Ain't that the pits! You fell in a pit! You now have {self.hit_points} HP.")
    elif room_content == "V":
      self.vision_potions += 1
      print("You found a vision potion!")
    elif room_content == "H":
      self.healing_potions += 1
      print("You found a healing potion!")
    elif room_content == "M":
      self.vision_potions += 1
      self.healing_potions += 1
      print("Wow! You found a healing AND a vision potion!")

    elif room_content == "A" and "A" not in self.pillar_pieces_found:
      self.pillar_pieces_found.append(room_content)
      print(f"You found the {room_content} pillar!")
    elif room_content == "P" and "P" not in self.pillar_pieces_found:
      self.pillar_pieces_found.append(room_content)
      print(f"You found the {room_content} pillar!")
    elif room_content == "E" and "E" not in self.pillar_pieces_found:
      self.pillar_pieces_found.append(room_content)
      print(f"You found the {room_content} pillar!")
    elif room_content == "I" and "I" not in self.pillar_pieces_found:
      self.pillar_pieces_found.append(room_content)
      print(f"You found the {room_content} pillar!")

    elif room_content == " ":
      print("There was nothing in the room!")
    elif room_content == "i":
      print("This is where you entered the dungeon!")
    elif room_content == "O":
      if "P" in self.pillar_pieces_found and "E" in self.pillar_pieces_found and "I" in self.pillar_pieces_found and "A" in self.pillar_pieces_found:
        print('Hooray!!!! You collected all pillars and found the exit!!!')
        print('~~ YOU WIN! ~~')
        print("Your ending stats:")
        print(self.__str__())
        self.alive = False
      else:
        print("This is where you can exit the dungeon... but you need to have all four pillars (A, P, I, E)!")
        print(f"Right now, you have: ")
        for pillar in self.pillar_pieces_found:
            print(pillar)

  def hp_increase(self):
    """
    hp_increase(self) method that increases the Hit Points accordingly, Healing Potion heals 5-15 hit points
      parameters: None
      return: None
    """
    self.hit_points += random.randint(5, 15)

  def hp_decrease(self):
    """
    hp_decrease(self) method that decreases the Hit Points accordingly, damage a pit can cause is from 1-20 hit points
      parameters: None
      return: None
    """
    if self.test_mode:
      self.hit_points -= 100000000000
    else:
      self.hit_points -= random.randint(1, 20)

    if self.hit_points <= 0:
      print("===== YOU DIED =====")
      print("Your ending stats:")
      print(self.__str__())
      self.alive = False

