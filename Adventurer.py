"""
Adventurer

NOTE: The Adventurer and the Dungeon will need to interact. When the Adventurer walks into a room if there is a potion in
the room, the Adventurer automatically picks up the potion. Likewise if there is a pit in the room, the Adventurer automatically
falls in the pit and takes a Hit Point loss. These changes obviously affect the room. For example, the Adventurer walks into a
room that contains a Healing Potion. The Adventurer will pick up the potion, changing the Adventurer's potion total, as well as
changing the room's potion total.
"""

import random

class Adventurer():
  """
  • Has a name
  • Contains at least the following:
    o Hit Points - initially set to 75 - 100 upon creation (randomly generate - you can change the range)
    o The number of Healing Potions
    o The number of Vision Potions
    o The which Pillars found
  """
  healing_potions = 0
  vision_potions = 0
  pillar_pieces_found = []

  def __init__(self, name):
    self.name = name
    self.hit_points = random.randint(75, 100)

  def __str__(self):
    """
    a __str__() method that builds a String containing:
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

    return f"{self.name} has {self.hit_points} hp\n\nThey have collected:\n* {self.healing_potions} healing potions\n* {self.vision_potions} vision potions\n* {pillars_string}"

  def move(self):
    """
    Ability to move in Dungeon (you might decide to place this behavior elsewhere)
    """
    pass

  def hp_change(self):
    """
    Increases or decreases the Hit Points accordingly
    """
    pass

a = Adventurer("Red")
print(a.__str__())