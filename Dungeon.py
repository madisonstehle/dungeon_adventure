import random
from Room import Room

class Dungeon:
  """
  • Creates/contains a maze of Rooms
    o The maze should be randomly generated
        ▪ You must incorporate an algorithm to ensure traversal of the maze from entrance to exit is possible once the
        maze has been generated. If the maze is not traversable, then generate a new one
    o The maze should have ‘dead ends’ (places that lead no further)
    o The type of data structure you use to represent your maze is up to you
        ▪ A list of lists has some advantages
        ▪ A linked list of linked lists has other advantages
        ▪ You could represent your maze via rooms that have references to other rooms (this would be much like a
        linked list structure but without all the basic linked list functionality which you do not need for this
        assignment)
  • Places the Entrance, the Exit, and the Pillars. NOTES: the entrance and exit are empty rooms. The Pillars cannot be at
  the entrance or the exit. No two Pillars may be in the same room.
  • (Possibly) Maintains location of the Adventurer in the Dungeon
  • Contains a _ _ str _ _ () method that builds a String containing information about the entire dungeon.
  """

  def __init__(self, row_count, col_count):
    self.__maze = []
    self.__rowCount = row_count
    self.__colCount = col_count

    for r in range(0, self.__rowCount):
      self.__maze.append([Room() for c in range(0, self.__colCount)])

    self.build_maze()

  def build_maze(self):
    # SKELETON CODE THAT IS PROOF OF CONCEPT
    # EACH INDIVIDUAL TASK SHOULD GO IN ITS OWN METHOD
    # CODE BELOW DOES NOT HAVE ERROR CHECKING

    # make some rooms impassible
    # rand gen chance a room is impassable
    # GIGANTIC NOTE: AFTER MAKING ROOMS IMPASSABLE YOU NEED TO CHECK TO SEE IF YOU CAN TRAVERSE MAZE
    # >>IF NOT YOU NEED TO RESET IMPASSABLE ROOMS
    for row in range(0, self.__rowCount):
      for col in range(0, self.__colCount):
        number = random.randint(1, 100)
        if number > 80:  # x% chance a room is impassable
          self.__maze[row][col].set_impassible(True)

    # set entrance and exit, make sure you make room passable
    self.__maze[0][0].set_entrance()
    self.__maze[0][0].set_impassible(False)
    self.__maze[self.__rowCount - 1][self.__colCount - 1].set_exit()
    self.__maze[self.__rowCount - 1][self.__colCount - 1].set_impassible(False)

    # place pillars after entrance/exit, watch for impassable

    # place health potions
    # could also do vision and pits
    for row in range(0, self.__rowCount):
      for col in range(0, self.__colCount):
        # make sure room not impassible
        if self.__maze[row][col].can_enter():
          # generate a random value
          number = random.randint(1, 100)
          if self.__maze[row][col].get_health_chance() >= number:
            self.__maze[row][col].set_health(True)

  def print_maze(self):
    # print(self.__maze)
    for row in range(0, self.__rowCount):
      print("row ", row)
      for col in range(0, self.__colCount):
        print("col", col)
        print(self.__maze[row][col].__str__())
      print()

  def set_health_potion(self, row, col):
    self.__maze[row][col].set_health(True)

  # WARNING: Work in progress ;-)
  # initial call if you know entrance is 0,0 would be traverse(0, 0)
  def traverse(self, row, col):
    found_exit = False
    if self.is_valid_room(row, col):
      self.__maze[row][col].set_visited(True)
      # check for exit
      if self.__maze[row][col].is_exit():
        return True
      # not at exit so try another room: south, east, north, west
      found_exit = self.traverse(row + 1, col)  # south
      if not found_exit:
        found_exit = self.traverse(row, col + 1)  # east
      if not found_exit:
        found_exit = self.traverse(row - 1, col)  # north
      if not found_exit:
        found_exit = self.traverse(row, col - 1)  # west

      # if we did not reach the exit from this room we need mark it as visited to
      # avoid going into the room again
      if not found_exit:
        self.__maze[row][col].set_visited(True)

    else:  # tried to move into a room that is not valid
      return False
    return found_exit

  def is_valid_room(self, row, col):
    return 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount and self.__maze[row][col].can_enter()

  def get_room(self, row, col):
    if 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount:
      return self.__maze[row][col]
