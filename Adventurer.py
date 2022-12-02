import random

class Adventurer:
  """
  • Has a name
  • Contains at least the following:
    o Hit Points - initially set to 75 - 100 upon creation (randomly generate - you can change the range)
    o The number of Healing Potions
    o The number of Vision Potions
    o The which Pillars found

  NOTE: The Adventurer and the Dungeon will need to interact. 

  When the Adventurer walks into a room if there is a potion in the room, 
  the Adventurer automatically picks up the potion. 

  Likewise if there is a pit in the room, the Adventurer automatically
  falls in the pit and takes a Hit Point loss. 

  These changes obviously affect the room. For example, the Adventurer walks into a
  room that contains a Healing Potion. The Adventurer will pick up the potion, 
  changing the Adventurer's potion total, as well as changing the room's potion total.
  """
  healing_potions = 5
  vision_potions = 0
  pillar_pieces_found = []

  def __init__(self, name):
    self.name = name
    self.hit_points = random.randint(75, 100)

  def __str__(self):
    """
    a _ _ str _ _ () method that builds a String containing:
      o Name
      o Hit Points
      o Total Healing Potions
      o Total Vision Potions
      o List of Pillars Pieces Found
    """
    pillars_string = ""

    if self.pillar_pieces_found:
      for pillar in self.pillar_pieces_found:
        if pillar is not self.pillar_pieces_found[len(self.pillar_pieces_found) - 1]:
          pillars_string += f"pillar {pillar}, "
        else:
          pillars_string += f"pillar {pillar}"
    else:
     pillars_string = "No pillars found yet! Get exploring!"

    return f"{self.name} has {self.hit_points} hp\nThey have collected:\n* {self.healing_potions} healing potions\n* {self.vision_potions} vision potions\n* {pillars_string}\n"

  def move(self):
    """
    Ability to move in Dungeon (you might decide to place this behavior elsewhere)
    """
    # SO FUN FACT colab doesn't use version 3.10 of python so the following code throws an error HOORAY
    key = input(
      "a, w, s, d to move your adventurer | h to use healing potion | v to use vision potion | i to see adventurer information\n")

    match key:
      case "a":
        print("moving left")
      case "w":
        print("moving up")
      case "s":
        print("moving down")
      case "d":
        print("moving right")
      case "h":
        if self.healing_potions != 0:
          self.hp_increase()
          print(f"You used a health potion! Your HP is now {self.hit_points}")
          self.healing_potions -= 1
        else:
          print("You don't have any healing potions!")
        self.move()
      case "v":
        if self.vision_potions != 0:
          # do the vision potion work here
          print("You used a vision potion!")
          self.vision_potions -= 1
        else:
          print("You don't have any vision potions!")
        self.move()
      case "i":
        print(self.__str__())
        self.move()  
      case _:
        self.move()

  def hp_increase(self):
    """
    Increases the Hit Points accordingly, Healing Potion heals 5-15 hit points
    """
    self.hit_points += random.randint(5, 15)

  def hp_decrease(self):
    """
    Decreases the Hit Points accordingly, damage a pit can cause is from 1-20 hit points
    """
    self.hit_points -= random.randint(1, 20)

